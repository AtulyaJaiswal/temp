import os
import replicate
# import openai

# audio_file= open(r"C:\Users\atuly\Downloads\test.mp3", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
replicate.client(api_token="de6b7412d8592848be2b55c552dad98c71109a4a")
replicate.run(
  "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
  input={"prompt": "a 19th century portrait of a wombat gentleman"}
)