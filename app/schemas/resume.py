
from dataclasses import dataclass

from fastapi import  Form, File, UploadFile
from typing_extensions import Annotated
from pydantic import BaseModel


# ResumeInput = {
#     "resume": Annotated[UploadFile, File()],
#     "job_desc": Annotated[str, Form()],
#     "keywords": Annotated[str, Form()]
# }

class ResumeInput(BaseModel):
    resumePdf: str
    jobDesc: str
    keywords: str