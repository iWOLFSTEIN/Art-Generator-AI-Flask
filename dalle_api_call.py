import openai
from env.secrets import DALLE_API_KEY

openai.api_key = DALLE_API_KEY


def create_images(prompt):
  response = openai.Image.create(
  prompt=prompt,
  n=8,
  size="256x256"
  )

  return response


