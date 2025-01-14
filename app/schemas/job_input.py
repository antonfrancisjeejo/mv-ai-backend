from pydantic import BaseModel

class JobInput(BaseModel):
    jobTitle: str
    jobCategory: str
    jobSkills: str
    jobDes: str