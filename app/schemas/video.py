from pydantic import BaseModel

class VideoInput(BaseModel):
    videoUrl: str
    question: str
    desc: str