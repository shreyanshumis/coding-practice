import json

from groq import Groq

from ..config import settings
from ..schemas.meeting import MeetingAnalysis


SYSTEM_PROMPT = """You are a precise meeting analyst. Extract only information supported by the transcript. Distinguish explicit decisions from suggestions. Do not invent names, owners, deadlines, timestamps, or conclusions. Use null when an action owner, deadline, or source timestamp is not stated. Keep the summary concise while preserving important technical details. Action items must be concrete and action-oriented."""


def summarize_transcript(transcript: str) -> MeetingAnalysis:
    if not settings.groq_api_key:
        raise RuntimeError("GROQ_API_KEY is not configured")

    schema = MeetingAnalysis.model_json_schema()
    client = Groq(api_key=settings.groq_api_key)
    response = client.chat.completions.create(
        model=settings.summary_model,
        messages=[
            {
                "role": "system",
                "content": f"{SYSTEM_PROMPT}\nReturn JSON only and follow this schema exactly:\n{json.dumps(schema)}",
            },
            {"role": "user", "content": f"Analyze this meeting transcript:\n\n{transcript}"},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "meeting_analysis",
                "strict": True,
                "schema": schema,
            },
        },
        temperature=0.1,
    )
    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("The summary model did not return a valid analysis")
    return MeetingAnalysis.model_validate_json(content)
