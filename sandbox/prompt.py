import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agent_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Pose une question à l'agent : ")
    print("Réponse de l'agent :", agent_response(user_input))
