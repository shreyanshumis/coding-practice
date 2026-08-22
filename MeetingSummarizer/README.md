# SummaMeet

SummaMeet converts uploaded meeting recordings into timestamped transcripts and structured, action-oriented meeting intelligence.

## Features

- Audio and video upload for AAC, MP3, WAV, M4A, MP4, MPEG, MPGA, OGG, FLAC, and WEBM
- Automatic AAC conversion to mono 16 kHz FLAC before transcription
- Persistent SQLite meeting storage
- Background transcription and summarization pipeline
- Groq speech-to-text integration with timestamped segments
- Structured LLM output for summaries, key points, decisions, tasks, owners, deadlines, and unresolved questions
- Live processing status with frontend polling
- Meeting history dashboard
- Persistent action-item completion
- Text report export
- Meeting and uploaded-file deletion
- Word Error Rate evaluation utility
- Responsive React interface

## Architecture

```text
React + Vite
     |
     | REST + multipart upload
     v
FastAPI
     |
     +---- SQLite
     +---- Local upload storage
     +---- Background task
              |
              +---- Groq transcription
              +---- Structured LLM analysis
```

ASR and LLM processing are separate stages. The API returns a meeting identifier immediately, and the frontend polls the meeting resource while work continues.

## Setup

Requirements:

- Node.js 20 or later
- Python 3.11 or later
- Groq API key

Install dependencies:

```bash
npm install
npm run install:frontend
npm run install:backend
```

Copy the environment template:

```bash
copy backend\.env.example backend\.env
```

Set `GROQ_API_KEY` in `backend/.env`, then start both applications:

```bash
npm run dev
```

Open `http://localhost:5173`. FastAPI documentation is available at `http://localhost:8000/docs`.

## Environment

| Variable | Default | Purpose |
| --- | --- | --- |
| `GROQ_API_KEY` | Empty | Required for transcription and summarization |
| `AI_PROVIDER` | `groq` | AI provider reported by the health endpoint |
| `TRANSCRIPTION_MODEL` | `whisper-large-v3-turbo` | Audio transcription model |
| `SUMMARY_MODEL` | `openai/gpt-oss-20b` | Structured meeting analysis model served by Groq |
| `DATABASE_URL` | `sqlite:///./meeting_summarizer.db` | SQLAlchemy database connection |
| `UPLOAD_DIRECTORY` | `uploads` | Local recording storage |
| `MAX_UPLOAD_MB` | `25` | Upload size limit aligned with Groq's free plan |

Raw AAC files are converted locally with the bundled FFmpeg runtime because the transcription endpoint does not accept `.aac` directly. The original AAC upload remains stored while the temporary FLAC is removed after processing.

## API

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Service and API-key readiness |
| `POST` | `/api/meetings` | Upload a meeting recording |
| `GET` | `/api/meetings` | List meetings |
| `GET` | `/api/meetings/{id}` | Retrieve transcript, analysis, and status |
| `PATCH` | `/api/meetings/{id}/actions/{action_id}` | Update action completion |
| `DELETE` | `/api/meetings/{id}` | Delete a meeting and recording |

## Prompt design

The analysis prompt enforces five rules that improve evaluation quality:

1. Extract only transcript-supported information.
2. Separate explicit decisions from suggestions.
3. Never invent owners, deadlines, timestamps, or conclusions.
4. Return null for missing action-item fields.
5. Produce schema-validated summary, points, decisions, actions, and unresolved questions.

The backend requests JSON output from Groq and validates it against a Pydantic schema. This makes the response predictable for the frontend and rejects missing or malformed fields.

## Evaluation

`backend/app/evaluation.py` provides `word_error_rate(reference, hypothesis)` for transcription evaluation.

Use a small representative audio set with human transcripts and report:

```text
WER = (substitutions + deletions + insertions) / reference words
```

Review summaries on a five-point rubric for factual accuracy, important-point coverage, decision extraction, action extraction, and absence of hallucinations. Compare prompt revisions against the same transcripts.

## Production progression

The MVP uses FastAPI background tasks, SQLite, and local files. For production, migrate to PostgreSQL, object storage, and a durable Redis/Celery worker queue without changing the frontend API contract.

## Demo video outline

1. Open the empty dashboard.
2. Upload a supported meeting recording.
3. Show the transcribing and summarizing stages.
4. Open the completed summary and transcript.
5. Review decisions and action items.
6. Complete an action item and export the report.
7. Show the FastAPI documentation and project structure.
