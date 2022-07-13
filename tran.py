import torch
from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

while True:
    prompt = input("==> ")

    res = generator(prompt, max_length=100, do_sample=True, temperature=0.9)
    print(res[0]['generated_text'])
