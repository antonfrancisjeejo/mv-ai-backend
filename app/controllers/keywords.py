from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def keywords_controller(input):

        jobTitle = input.jobTitle
        jobDesc = input.jobDesc
        jobCategory = input.jobCategory
        jobSkills = input.jobSkills


        promptTemplate = f"""
        Act as a hiring expert. I will provide you with a job description, and your task is to extract important keywords from the job title and job category to match with resumes. Your goal is to identify essential keywords, such as skills, technologies, and tech stacks, from the given job title, description, category and skills. Return exactly 15 keywords not more or less, exactly 15 keywords in json format. Json's key will be "keywords" which returns a list of keywords
        Here is the job title:
        {jobTitle}

        Job Category:
        {jobCategory}

        Job Description:
        {jobDesc}

        Job skills:
        {jobSkills}

        """

        client = OpenAI()

        completion = client.chat.completions.create(
                model="o1-mini",
                messages=[
                        {
                                "role": "user",
                                "content": promptTemplate
                        }
                ]
        )

        response = (completion.choices[0].message.content).replace("```json", "").replace("```", "")
        return response