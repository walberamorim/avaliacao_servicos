import urllib.request as requisicao
import json
from time import sleep

# URLs dos serviços
URL_SERVICO_TI = "http://127.0.0.1:5001/"
URL_SERVICO_SAUDE = "http://127.0.0.1:5002/"
URL_SERVICO_COMERCIAL = "http://127.0.0.1:5003/"

# Endpoints para vagas
URL_VAGAS_TI = URL_SERVICO_TI + "vagas"
URL_VAGAS_SAUDE = URL_SERVICO_SAUDE + "vagas"
URL_VAGAS_COMERCIAL = URL_SERVICO_COMERCIAL + "vagas"

# Endpoints para verificação de status
URL_ALIVE_TI = URL_SERVICO_TI + "alive"
URL_ALIVE_SAUDE = URL_SERVICO_SAUDE + "alive"
URL_ALIVE_COMERCIAL = URL_SERVICO_COMERCIAL + "alive"

def acessar(url):
    sucesso, conteudo = False, None
    try:
        resposta = requisicao.urlopen(url)
        if resposta.status == 200:
            conteudo = resposta.read().decode("utf-8")
            sucesso = True
    except:
        print(f"Ocorreu um erro ao acessar a url: {url}")
    return sucesso, conteudo

def get_vagas_ti():
    sucesso, vagas = acessar(URL_VAGAS_TI)
    if sucesso:
        vagas = json.loads(vagas)
    else:
        print("Ocorreu um erro ao obter as vagas de TI")
        vagas = []
    return vagas

def get_vagas_saude():
    sucesso, vagas = acessar(URL_VAGAS_SAUDE)
    if sucesso:
        vagas = json.loads(vagas)
    else:
        print("Ocorreu um erro ao obter as vagas de Saúde")
        vagas = []
    return vagas

def get_vagas_comercial():
    sucesso, vagas = acessar(URL_VAGAS_COMERCIAL)
    if sucesso:
        vagas = json.loads(vagas)
    else:
        print("Ocorreu um erro ao obter as vagas Comerciais")
        vagas = []
    return vagas

def servico_ti_ativo():
    sucesso, ativo = acessar(URL_ALIVE_TI)
    return sucesso and ativo == "sim"

def servico_saude_ativo():
    sucesso, ativo = acessar(URL_ALIVE_SAUDE)
    return sucesso and ativo == "sim"

def servico_comercial_ativo():
    sucesso, ativo = acessar(URL_ALIVE_COMERCIAL)
    return sucesso and ativo == "sim"

def imprimir_vagas(setor, vagas):
    print(f"\n===== VAGAS DISPONÍVEIS NO SETOR DE {setor.upper()} =====")
    if not vagas:
        print(f"Nenhuma vaga disponível no setor de {setor}.")
        return
    
    for contador, vaga in enumerate(vagas, 1):
        print(f"\nVaga {contador}")
        print(f"ID: {vaga['id']}")
        print(f"Data: {vaga['data_publicacao']}")
        print(f"Título: {vaga['titulo']}")
        print(f"Empresa: {vaga['empresa']}")
        print(f"Salário: {vaga['salario']}")
        print(f"Local: {vaga['local']}")
        print(f"Descrição: {vaga['descricao']}")
        print(f"Requisitos: {', '.join(vaga['requisitos'])}")
        print(f"Contato: {vaga['contato']}")
        print("-" * 50)

if __name__ == "__main__":
    print("Portal de Vagas - Iniciando consulta...")
    
    while True:
        servicos_ativos = False
        
        if servico_ti_ativo():
            imprimir_vagas("TI", get_vagas_ti())
            servicos_ativos = True
            
        if servico_saude_ativo():
            imprimir_vagas("Saúde", get_vagas_saude())
            servicos_ativos = True
            
        if servico_comercial_ativo():
            imprimir_vagas("Comercial", get_vagas_comercial())
            servicos_ativos = True
            
        if not servicos_ativos:
            print("Todos os serviços estão inativos no momento.")
            
        print("\nAtualizando em 5 segundos...")
        sleep(5)