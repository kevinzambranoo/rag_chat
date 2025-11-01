import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Crear cliente de OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)



def get_rag_response(message: str, context_text: str):
    """
    Usa el texto del archivo como contexto adicional
    para responder a la pregunta del usuario.
    """
    print("text "+context_text)
    prompt = f"""
        Eres un asistente inteligente. Usa el siguiente texto como referencia para responder con precisión:

        --- CONTEXTO ---
        {context_text}
        -----------------

        Pregunta del usuario:
        {message}
    """

    # Llamada al modelo (puedes usar gpt-4o-mini o gpt-3.5-turbo según tu plan)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {"role": "system", "content": "Eres un experto en análisis de texto."},
            {"role": "user", "content": prompt},
        ],
    )

    # Devolver texto plano
    return response.choices[0].message.content.strip()