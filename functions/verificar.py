from functions.encaminhar import msg_analista, msg_ingredientes, msg_precificacao, msg_financeiro

def verificar_mensagem(assunto):
    assunto_verificar = assunto.strip().lower()
    if assunto_verificar.endswith('análise de vendas'):
        msg_analista(assunto)
    elif assunto_verificar.endswith('ingredientes'):
        msg_ingredientes(assunto)
    elif assunto_verificar.endswith('precificação'):
        msg_precificacao(assunto)
    elif assunto_verificar.endswith('de gestão'):
        msg_financeiro(assunto)
    else:
        print('❗ Erro em Verificar a Mensagem')