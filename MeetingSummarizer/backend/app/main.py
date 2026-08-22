from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.meetings import router as meetings_router
from .config import settings
from .database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="SummaMeet API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(meetings_router, prefix="/api")


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "provider": settings.ai_provider,
        "groq_configured": bool(settings.groq_api_key),
    }
