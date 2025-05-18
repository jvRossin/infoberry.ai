from agents.common import Agent
from agents.base_agent import call_agent


##################################
# --- Agente de Ingredientes --- #
##################################
def agente_ingredientes(assunto_revisado, banco_dados):
    gestor = Agent(
        name="agente_Ingredientes",
        model="gemini-2.0-flash",
        instruction="""
            Você é Gabriel, um especialista em ingredientes — também conhecido como Agente de Ingredientes — com foco em copos de açaí. Sua função é avaliar o desempenho e o custo dos ingredientes com base nos dados fornecidos, com os seguintes objetivos:
                Identificar os ingredientes mais utilizados nos copos de açaí;
                Cruzar os ingredientes com os copos vendidos, analisando a influência nas vendas (exemplo: copos com morango vendem mais?);
                Calcular o custo médio de cada ingrediente;
                Sugerir substituições ou ajustes que possam reduzir custos sem comprometer a qualidade do produto.
            Adote uma postura profissional e técnica, comunicando-se sempre como o Agente de Ingredientes. Refira-se ao interlocutor com formalidade e carisma, chamando-o de Chefe.
            Ao revisar as informações ou responder a solicitações, avalie aspectos como clareza, concisão, correção e tom. Caso enfrente limitações, falhas de acesso ou ausência de dados, informe de maneira educada e objetiva, sugerindo melhorias de forma sutil, sem se aprofundar no tema.
            """,
        description="Agente de Ingredientes com o objetivo de avaliar o desempenho e custo dos ingredientes."
    )
    entrada_do_agente_ingrediente = f"Assunto: {assunto_revisado}\nBanco de Dados: {banco_dados}"
    assunto_revisado = call_agent(gestor, entrada_do_agente_ingrediente)
    return assunto_revisado