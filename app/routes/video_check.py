import json

from fastapi import APIRouter
from app import controllers
from app.schemas import VideoInput

router = APIRouter()

@router.post("")
def assess_video(input:VideoInput):
    feedback = json.loads(controllers.video_controller(input))
    return feedback
