import os
import sys
import time
from dotenv import load_dotenv
from google import genai
from functions.iniciar_chat import iniciar_chat
from functions.verificar import verificar_mensagem


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)


caracteres_animacao = ['/', '-', '\\', '|']
tempo_espera = 0.1
duracao = 5
inicio = time.time()

while time.time() - inicio < duracao:
    for caractere in caracteres_animacao:
        if time.time() - inicio >= duracao:
            break
        print(f"\r🚀 Iniciando Sistema Stanley {caractere}   ", end='', flush=True)
        time.sleep(tempo_espera)
print('\n')
print("🥶 Sistema de Gestão Stanley Iniciado 🥣")
prompt = input("Por favor, digite o Assunto sobre o qual você quer gerir: ")

if not prompt:
    print("❗O Assunto não foi válido para prosseguir!")
    prompt = input("Por favor, digite novamente o Assunto sobre o qual você quer gerir: ")
else:
    prompt_buscado = iniciar_chat(prompt)

verificar_mensagem(prompt_buscado)
