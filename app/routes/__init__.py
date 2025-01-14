from fastapi import APIRouter

from app.routes import keywords
from app.routes import resume

api_router = APIRouter()
api_router.include_router(keywords.router, prefix="/keywords", tags=["keywords"])
api_router.include_router(resume.router, prefix="/resume", tags=["resume"])
