from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url = 'https://openrouter.ai/api/v1',
    api_key = API_KEY
)

def enviar_mensagem(mensagem, lista_mensagens): 
    lista_mensagens.append({'role': 'user', 'content': mensagem})
    lista_mensagens.append({'role': 'system', 'content': 'Você é um assistente útil e amigável.'})
  
    resposta = client.chat.completions.create(
        model = 'z-ai/glm-4.5-air:free',
        messages = lista_mensagens
    )
    return resposta.choices[0].message

lista_mensagens = []

while True:
    entrada_usuario = input("Você: ")

    if entrada_usuario.upper().split() == ['SAIR']:
        print("Chatbot: Até mais!")
        break
    else:
        resposta_chatbot = enviar_mensagem(entrada_usuario, lista_mensagens)
        lista_mensagens.append(resposta_chatbot)
        print("Chatbot:", resposta_chatbot.content)