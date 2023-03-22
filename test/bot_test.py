import os
import openai
from sys import argv

if len(argv) == 1:
    print('Please Give Model ID')
    quit()
model_id = argv[1]

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion.create(model=model_id, prompt=input("Prompt: "))

print(completion['choices'][0]['text'])