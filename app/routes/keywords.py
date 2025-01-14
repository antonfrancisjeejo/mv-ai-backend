import json

from fastapi import APIRouter
from app import controllers
from app.schemas import JobInput

router = APIRouter()


@router.post("")
def get_keywords(input:JobInput):
    keywords = json.loads(controllers.keywords_controller(input))
    return keywords
