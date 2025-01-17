from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
from PyPDF2 import PdfReader, PdfWriter
from urllib.request import Request, urlopen
from io import BytesIO
import os
import random
import time

load_dotenv()

async def resume_controller(resumePdf, job_desc, keywords):
    writer = PdfWriter()

    remoteFile = urlopen(Request(resumePdf)).read()
    memoryFile = BytesIO(remoteFile)
    pdfFile = PdfReader(memoryFile)

    for page in pdfFile.pages:
        writer.add_page(page)

    num = int(random.random() * time.time() * 5)
    file_name = "output_" + str(num)+ ".pdf"

    with open(file_name, "wb") as outputStream:
        writer.write(outputStream)
    reader = PdfReader(file_name)
    resume = ""

    for page in reader.pages:
        resume += page.extract_text()

    prompt = f"Given the Resume and Job Description, your task is to tell the percentage and feedback on how much the person's resume matches with the job description. The job description is: {job_desc}. Do not mix up the resume with the job description; both are separate. Take keywords from the job description and try to search for them in the resume also check resume with this given job related keywords {keywords} . If keywords are not found, the person is not suitable based on the number of important job keywords that match, and you must give a percentage of 0-100. Here is the resume: {resume}. The job description is already given above. If the resume doesn't have that important word just leave it. The percentage can even be 10 or below also if the important keywords from job doesn't match well. For example if the job description has SAP and resume doesn't then you should reject the resume. THe feedback can be negative also if keyword doesn't match. If the job description is development and the resume has cybersecurity the you can just throw 10-15 precent directly but if the resume has the development with experience you required then you can give more percentage even 85+. it's upto you. Give in json format with 3 keys - percentage , feedback, suitable with yes or no"

    client = OpenAI()

    completion = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = (completion.choices[0].message.content).replace("```json", "")
    output = output.replace("```", "")
    os.remove(file_name)
    return output