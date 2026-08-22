import re
from pathlib import Path

from fastapi import APIRouter, BackgroundTasks, Depends, File, Form, HTTPException, Response, UploadFile, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from ..config import settings
from ..database import get_db
from ..models.meeting import ActionItem, Meeting
from ..schemas.meeting import ActionItemResponse, ActionItemUpdate, MeetingCreated, MeetingDetail, MeetingListItem
from ..workers.tasks import process_meeting


router = APIRouter(prefix="/meetings", tags=["meetings"])
allowed_extensions = {".aac", ".flac", ".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".ogg", ".wav", ".webm"}


def to_list_item(meeting: Meeting) -> MeetingListItem:
    return MeetingListItem(
        **meeting.__dict__,
        action_item_count=len(meeting.action_items),
    )


@router.post("", response_model=MeetingCreated, status_code=status.HTTP_202_ACCEPTED)
def create_meeting(
    background_tasks: BackgroundTasks,
    audio: UploadFile = File(...),
    title: str | None = Form(None),
    db: Session = Depends(get_db),
):
    extension = Path(audio.filename or "").suffix.lower()
    if extension not in allowed_extensions:
        raise HTTPException(status_code=415, detail="Unsupported audio format")

    safe_stem = re.sub(r"[^a-zA-Z0-9_-]+", "-", Path(audio.filename or "meeting").stem).strip("-") or "meeting"
    meeting = Meeting(
        title=(title or Path(audio.filename or "Untitled meeting").stem).strip()[:180],
        filename=(audio.filename or f"meeting{extension}")[:255],
        stored_filename="pending",
        content_type=audio.content_type,
    )
    db.add(meeting)
    db.flush()

    settings.upload_path.mkdir(parents=True, exist_ok=True)
    stored_filename = f"{meeting.id}-{safe_stem}{extension}"
    destination = settings.upload_path / stored_filename
    max_bytes = settings.max_upload_mb * 1024 * 1024
    written = 0
    try:
        with destination.open("wb") as output:
            while chunk := audio.file.read(1024 * 1024):
                written += len(chunk)
                if written > max_bytes:
                    raise HTTPException(status_code=413, detail=f"File exceeds {settings.max_upload_mb} MB")
                output.write(chunk)
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    finally:
        audio.file.close()

    meeting.stored_filename = stored_filename
    db.commit()
    background_tasks.add_task(process_meeting, meeting.id, str(destination))
    return MeetingCreated(meeting_id=meeting.id, status=meeting.status)


@router.get("", response_model=list[MeetingListItem])
def list_meetings(db: Session = Depends(get_db)):
    query = select(Meeting).options(selectinload(Meeting.action_items)).order_by(Meeting.created_at.desc())
    return [to_list_item(meeting) for meeting in db.scalars(query).all()]


@router.get("/{meeting_id}", response_model=MeetingDetail)
def get_meeting(meeting_id: str, db: Session = Depends(get_db)):
    query = select(Meeting).where(Meeting.id == meeting_id).options(selectinload(Meeting.action_items))
    meeting = db.scalar(query)
    if meeting is None:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return MeetingDetail(**to_list_item(meeting).model_dump(), **{
        "language": meeting.language,
        "transcript": meeting.transcript,
        "transcript_segments": meeting.transcript_segments or [],
        "key_points": meeting.key_points or [],
        "decisions": meeting.decisions or [],
        "unresolved_questions": meeting.unresolved_questions or [],
        "error_message": meeting.error_message,
        "completed_at": meeting.completed_at,
        "action_items": meeting.action_items,
    })


@router.patch("/{meeting_id}/actions/{action_id}", response_model=ActionItemResponse)
def update_action(meeting_id: str, action_id: str, payload: ActionItemUpdate, db: Session = Depends(get_db)):
    action = db.scalar(select(ActionItem).where(ActionItem.id == action_id, ActionItem.meeting_id == meeting_id))
    if action is None:
        raise HTTPException(status_code=404, detail="Action item not found")
    action.completed = payload.completed
    db.commit()
    db.refresh(action)
    return action


@router.delete("/{meeting_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meeting(meeting_id: str, db: Session = Depends(get_db)):
    meeting = db.get(Meeting, meeting_id)
    if meeting is None:
        raise HTTPException(status_code=404, detail="Meeting not found")
    path = settings.upload_path / meeting.stored_filename
    db.delete(meeting)
    db.commit()
    path.unlink(missing_ok=True)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
