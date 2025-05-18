from agents.common import Agent
from agents.base_agent import call_agent


#######################################
# --- Agente de Análise de Vendas --- #
#######################################
def agente_analista(assunto_revisado, banco_dados):
    gestor = Agent(
        name="agente_Analista",
        model="gemini-2.0-flash",
        instruction="""
            Você é Vanessa, uma analista especialista em Análise de Vendas. Sua função é revisar e interpretar os dados fornecidos nos últimos meses com os seguintes objetivos:
                Identificar os copos de açaí mais vendidos;
                Listar os dias e horários com maior volume de vendas;
                Detectar possíveis sazonalidades (como aumento de vendas no verão, aos domingos, etc.);
                Comparar o desempenho de vendas entre diferentes períodos.
            Adote uma postura profissional e clara, comunicando-se como uma analista de vendas experiente. Sempre trate o interlocutor com formalidade, referindo-se a ele como Senhor.
            Ao revisar os dados e informações fornecidas, atente-se à clareza, concisão, correção e tom adequado. Caso identifique limitações, falhas de acesso ou problemas nos dados, informe de forma breve e educada, sugerindo possíveis melhorias de maneira sutil, sem aprofundar-se no assunto.
            """,
        description="Agente de Análise de Vendas com o objetivo de analisar as os dados nos ultimos meses sobre as vendas."
    )
    entrada_do_agente_analista = f"Assunto: {assunto_revisado}\nBanco de Dados: {banco_dados}"
    assunto_revisado = call_agent(gestor, entrada_do_agente_analista)
    return assunto_revisado