import json
from operator import itemgetter

from app import controllers
from app.schemas import ResumeInput
from fastapi import APIRouter

router = APIRouter()


# async def resume_check(
#     resumePdf: ResumeInput["resume"],
#     job_desc: ResumeInput["job_desc"],
#     keywords: ResumeInput["keywords"],
# ):
#         response = json.loads(await controllers.resume_controller(resumePdf, job_desc, keywords))
#         return response

@router.post("/check")
async def resume_check(input:ResumeInput):
        response = json.loads(await controllers.resume_controller(input.resumePdf, input.jobDesc, input.keywords))
        return response