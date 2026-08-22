import enum
import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, DateTime, Enum, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class MeetingStatus(str, enum.Enum):
    uploaded = "uploaded"
    transcribing = "transcribing"
    summarizing = "summarizing"
    completed = "completed"
    failed = "failed"


class Meeting(Base):
    __tablename__ = "meetings"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(180))
    filename: Mapped[str] = mapped_column(String(255))
    stored_filename: Mapped[str] = mapped_column(String(255))
    content_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    status: Mapped[MeetingStatus] = mapped_column(Enum(MeetingStatus), default=MeetingStatus.uploaded)
    duration_seconds: Mapped[float | None] = mapped_column(Float, nullable=True)
    language: Mapped[str | None] = mapped_column(String(20), nullable=True)
    transcript: Mapped[str | None] = mapped_column(Text, nullable=True)
    transcript_segments: Mapped[list] = mapped_column(JSON, default=list)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    key_points: Mapped[list] = mapped_column(JSON, default=list)
    decisions: Mapped[list] = mapped_column(JSON, default=list)
    unresolved_questions: Mapped[list] = mapped_column(JSON, default=list)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    action_items: Mapped[list["ActionItem"]] = relationship(back_populates="meeting", cascade="all, delete-orphan")


class ActionItem(Base):
    __tablename__ = "action_items"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    meeting_id: Mapped[str] = mapped_column(ForeignKey("meetings.id", ondelete="CASCADE"), index=True)
    task: Mapped[str] = mapped_column(Text)
    assignee: Mapped[str | None] = mapped_column(String(180), nullable=True)
    deadline: Mapped[str | None] = mapped_column(String(180), nullable=True)
    source_timestamp: Mapped[str | None] = mapped_column(String(20), nullable=True)
    completed: Mapped[bool] = mapped_column(default=False)
    meeting: Mapped[Meeting] = relationship(back_populates="action_items")
