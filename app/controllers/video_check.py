from dotenv import load_dotenv
from openai import OpenAI
# import moviepy.editor
from moviepy.editor import VideoFileClip
import urllib.request
import os
import random
import time

from app.schemas import VideoInput

load_dotenv()

def video_controller(input:VideoInput):

    dwn_link = input.videoUrl
    question = input.question
    jobDescription = input.desc
    num = int(random.random() * time.time() * 5)
    video_name = "video_" + str(num) + ".webm"
    audio_name = "audio_" + str(num) + ".mp3"

    # Download the file
    rsp = urllib.request.urlopen(dwn_link)
    with open(video_name, 'wb') as f:
        f.write(rsp.read())

    # Conversion from Video to Audio and storing it in a file
    client = OpenAI()
    os.system(f"""ffmpeg -i {video_name} {audio_name}""")

    # loading the open ai apikey into the environment

    # extracting the speech from the audio file using open ai whisper model
    audio_file = open(audio_name, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

    videoText = transcription.text

    qstn = f""""
        Question:
        {question}
        """

    promptTemplate = f"""
        I want you to check the correctness of the answer for the given question by checking with the answer and also checking whether the answer aligns with the given job description and rate it on a scale of 1-10. For example if the answer is relevant to the question but not relevant to the job description, then you should reduce the score accordingly not too much, but based on the accuracy and relevance.
        Here is the question: {qstn}
        Here is the answer: {videoText} .
        Here is the job description: {jobDescription}.

        Just return the score as 1-10 in json having a key score also return a feedback on the answer how its relevant or not relevant and tell what this person lack as its a interview answer from a candidate. feedback should be inside the feedback key


        """

    client = OpenAI()

    completion = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {
                "role": "user",
                "content": promptTemplate
            }
        ]
    )

    output = (completion.choices[0].message.content).replace("```json", "")
    output = output.replace("```", "")
    try:
        os.remove(video_name)
        os.remove(audio_name)
    except OSError as e:
        # If it fails, inform the user.
        print("Error: %s - %s." % (e.filename, e.strerror))
    return output