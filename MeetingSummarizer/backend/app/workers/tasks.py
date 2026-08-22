from datetime import datetime, timezone
from pathlib import Path

from ..database import SessionLocal
from ..models.meeting import ActionItem, Meeting, MeetingStatus
from ..services.audio import prepare_for_transcription
from ..services.summarization import summarize_transcript
from ..services.transcription import transcribe_audio


def process_meeting(meeting_id: str, audio_path: str):
    db = SessionLocal()
    prepared_path = Path(audio_path)
    remove_prepared = False
    try:
        meeting = db.get(Meeting, meeting_id)
        if meeting is None:
            return

        meeting.status = MeetingStatus.transcribing
        meeting.error_message = None
        db.commit()

        prepared_path, remove_prepared = prepare_for_transcription(Path(audio_path))
        transcription = transcribe_audio(prepared_path)
        meeting.transcript = transcription["text"]
        meeting.language = transcription["language"]
        meeting.duration_seconds = transcription["duration_seconds"]
        meeting.transcript_segments = transcription["segments"]
        meeting.status = MeetingStatus.summarizing
        db.commit()

        analysis = summarize_transcript(meeting.transcript)
        meeting.summary = analysis.summary
        meeting.key_points = analysis.key_points
        meeting.decisions = analysis.decisions
        meeting.unresolved_questions = analysis.unresolved_questions
        meeting.action_items = [ActionItem(**item.model_dump()) for item in analysis.action_items]
        meeting.status = MeetingStatus.completed
        meeting.completed_at = datetime.now(timezone.utc)
        db.commit()
    except Exception as error:
        db.rollback()
        meeting = db.get(Meeting, meeting_id)
        if meeting is not None:
            meeting.status = MeetingStatus.failed
            meeting.error_message = str(error)[:1000]
            db.commit()
    finally:
        if remove_prepared:
            prepared_path.unlink(missing_ok=True)
        db.close()
