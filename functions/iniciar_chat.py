from datetime import date
from agents.gestor import agente_gestor

data_de_hoje = date.today().strftime("%d/%m/%Y")

def iniciar_chat(assunto):
    print("\nMaravilha! Vamos então fazer a gestão sobre seu assunto")
    assunto_buscado = agente_gestor(assunto, data_de_hoje)
    
    print("\n--- 🧑‍💼 Resultado do Gestor ---\n")
    while not assunto_buscado.startswith('Entendido!'):
        print(assunto_buscado)
        print("--------------------------------------------------------------")
        print('\n')
        
        assunto = input("❗ Por favor, digite novamente: ")
        assunto_buscado = agente_gestor(assunto, data_de_hoje)
        
        print("\n--- 🧑‍💼 Resultado do Gestor ---\n")
    else:
        print(assunto_buscado)
    print("--------------------------------------------------------------")
    print('\n')
    return assunto_buscado