from datetime import datetime

from pydantic import BaseModel, ConfigDict

from ..models.meeting import MeetingStatus


class ActionItemAnalysis(BaseModel):
    task: str
    assignee: str | None
    deadline: str | None
    source_timestamp: str | None
    model_config = ConfigDict(extra="forbid")


class MeetingAnalysis(BaseModel):
    summary: str
    key_points: list[str]
    decisions: list[str]
    action_items: list[ActionItemAnalysis]
    unresolved_questions: list[str]
    model_config = ConfigDict(extra="forbid")


class ActionItemResponse(ActionItemAnalysis):
    id: str
    completed: bool
    model_config = ConfigDict(from_attributes=True)


class TranscriptSegment(BaseModel):
    start: float
    end: float
    text: str
    speaker: str | None = None


class MeetingListItem(BaseModel):
    id: str
    title: str
    filename: str
    status: MeetingStatus
    duration_seconds: float | None
    summary: str | None
    created_at: datetime
    action_item_count: int = 0
    model_config = ConfigDict(from_attributes=True)


class MeetingDetail(MeetingListItem):
    language: str | None
    transcript: str | None
    transcript_segments: list[TranscriptSegment]
    key_points: list[str]
    decisions: list[str]
    unresolved_questions: list[str]
    error_message: str | None
    completed_at: datetime | None
    action_items: list[ActionItemResponse]


class MeetingCreated(BaseModel):
    meeting_id: str
    status: MeetingStatus


class ActionItemUpdate(BaseModel):
    completed: bool
