from agents.analista import agente_analista
from agents.ingredientes import agente_ingredientes
from agents.precificacao import agente_precificacao
from agents.financeiro import agente_financeiro
from functions.common import banco_dados



def msg_analista(assunto):
    analise = agente_analista(assunto, banco_dados)
    print("\n--- 👩‍💼 Resultado do Agente - Vanessa - (Analista de Vendas) ---\n")
    print(analise)
    print("--------------------------------------------------------------")
    print('\n')
    
    novo_assunto = input("Continue a conversa ou digite 'Encerrar':")
    while not novo_assunto.startswith('Encerrar'):
        analise = agente_analista(novo_assunto, banco_dados)
        
        print("\n--- 👩‍💼 Resultado do Agente - Vanessa - (Analista de Vendas) ---\n")
        print(analise)
        print("--------------------------------------------------------------")
        print('\n')
        novo_assunto = input("Continue a conversa ou digite 'Encerrar': ")
    else:
        print('\nEspero que tenha ajudado!')



def msg_ingredientes(assunto):
    analise = agente_ingredientes(assunto, banco_dados)
    print("\n--- 🍌 Resultado do Agente - Gabriel - (Ingredientes) ---\n")
    print(analise)
    print("--------------------------------------------------------------")
    print('\n')
    
    novo_assunto = input("Continue a conversa ou digite 'Encerrar':")
    while not novo_assunto.startswith('Encerrar'):
        analise = agente_ingredientes(novo_assunto, banco_dados)
        
        print("\n--- 🍌 Resultado do Agente - Gabriel - (Ingredientes) ---\n")
        print(analise)
        print("--------------------------------------------------------------")
        print('\n')
        novo_assunto = input("Continue a conversa ou digite 'Encerrar': ")
    else:
        print('\nEspero que tenha ajudado!')



def msg_precificacao(assunto):
    analise = agente_precificacao(assunto, banco_dados)
    print("\n--- 📊 Resultado do Agente - Victor - (Custos e Precificação) ---\n")
    print(analise)
    print("--------------------------------------------------------------")
    print('\n')
    
    novo_assunto = input("Continue a conversa ou digite 'Encerrar':")
    while not novo_assunto.startswith('Encerrar'):
        analise = agente_precificacao(novo_assunto, banco_dados)
        
        print("\n--- 📊 Resultado do Agente - Victor - (Custos e Precificação) ---\n")
        print(analise)
        print("--------------------------------------------------------------")
        print('\n')
        novo_assunto = input("Continue a conversa ou digite 'Encerrar': ")
    else:
        print('\nEspero que tenha ajudado!')



def msg_financeiro(assunto):
    analise = agente_financeiro(assunto, banco_dados)
    print("\n--- 💰 Resultado do Agente - Daniel - (Financeiro e de Gestão) ---\n")
    print(analise)
    print("--------------------------------------------------------------")
    print('\n')
    
    novo_assunto = input("Continue a conversa ou digite 'Encerrar':")
    while not novo_assunto.startswith('Encerrar'):
        analise = agente_financeiro(novo_assunto, banco_dados)
        
        print("\n--- 💰 Resultado do Agente - Daniel - (Financeiro e de Gestão) ---\n")
        print(analise)
        print("--------------------------------------------------------------")
        print('\n')
        novo_assunto = input("Continue a conversa ou digite 'Encerrar': ")
    else:
        print('\nEspero que tenha ajudado!')