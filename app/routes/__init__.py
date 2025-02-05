from fastapi import APIRouter

from app.routes import keywords
from app.routes import resume
from app.routes import video_check

api_router = APIRouter()
api_router.include_router(keywords.router, prefix="/keywords", tags=["keywords"])
api_router.include_router(resume.router, prefix="/resume", tags=["resume"])
api_router.include_router(video_check.router, prefix="/video-check", tags=["video-assessment"])
