import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

models = client.models.list()
for model in models:
    print(model.id)