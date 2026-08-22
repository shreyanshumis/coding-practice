from pathlib import Path

from groq import Groq

from ..config import settings


def normalize_segments(segments: list) -> list[dict]:
    normalized = []
    for segment in segments:
        if isinstance(segment, dict):
            start = segment.get("start", 0)
            end = segment.get("end", start)
            text = segment.get("text", "")
        else:
            start = segment.start
            end = segment.end
            text = segment.text
        normalized.append(
            {
                "start": float(start),
                "end": float(end),
                "text": str(text).strip(),
                "speaker": None,
            }
        )
    return normalized


def transcribe_audio(path: Path) -> dict:
    if not settings.groq_api_key:
        raise RuntimeError("GROQ_API_KEY is not configured")

    client = Groq(api_key=settings.groq_api_key)
    with path.open("rb") as audio_file:
        response = client.audio.transcriptions.create(
            model=settings.transcription_model,
            file=audio_file,
            response_format="verbose_json",
            timestamp_granularities=["segment"],
        )

    segments = normalize_segments(response.segments or [])
    duration = float(response.duration) if response.duration is not None else None
    return {
        "text": response.text.strip(),
        "language": response.language,
        "duration_seconds": duration,
        "segments": segments,
    }
