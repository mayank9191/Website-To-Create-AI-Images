from openai import OpenAI
import requests
from io import BytesIO
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("openai-api-key")
client = OpenAI(api_key=openai_key)


def chatsearch(text):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a chat assistant."},
            {"role": "user", "content": text}
        ]
    )

    response = completion.choices[0].message.content
    return response


def imagecreate(description):
    # Used to Generate AI Images
    completion = client.images.generate(
        model="dall-e-3",
        prompt=description,
        n=1,
        size="1024x1024"
    )

    url = completion.data[0].url

    return url

    # -------------TO SAVE IMAGE AND VIEW IT  -----------------------------
    # response = requests.get(url=url)

    # image = Image.open(BytesIO(response.content))

    # image.show()

    # image.save("pic1.png")
