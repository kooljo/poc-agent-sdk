import openai
from openai import OpenAI
import os
import fitz

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_pdf(file_path):
    """Lit un fichier PDF et extrait son contenu sous forme de texte."""
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
        return text
    except Exception as e:
        return f"Erreur lors de la lecture du PDF : {e}"


def analyze_pdf_with_agent(pdf_content, question):
    """Envoie le contenu du PDF à l'agent et pose une question dessus."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un assistant spécialisé dans l'analyse de documents PDF."},
            {"role": "user", "content": f"Voici le contenu du fichier PDF :\n\n{pdf_content[:4000]}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    file_path = "cv.pdf"
    pdf_content = read_pdf(file_path)

    if pdf_content.startswith("Erreur"):
        print(pdf_content)
    else:
        print("Fichier PDF chargé avec succès !")
        user_question = input("Pose ta question sur le fichier PDF : ")
        response = analyze_pdf_with_agent(pdf_content, user_question)
        print("\nRéponse de l'agent :", response)
