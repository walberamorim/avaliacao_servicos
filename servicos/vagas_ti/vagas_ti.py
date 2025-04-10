from flask import Flask, Response
import json

VERSAO = "1.0.0"

INFO = {
    "descricao": "Serviço que disponibiliza vagas de emprego na área de TI",
    "autor": "Claude",
    "versao": VERSAO
}

VAGAS_TI = [
    {
        "id": "1",
        "data_publicacao": "10/04/2025",
        "titulo": "Desenvolvedor Full Stack",
        "empresa": "TechSolutions",
        "salario": "R$ 8.000 - R$ 10.000",
        "local": "São Paulo, SP (Híbrido)",
        "descricao": "Desenvolvedor com experiência em React, Node.js e Python para atuar em projetos inovadores",
        "requisitos": ["JavaScript", "React", "Node.js", "Python", "MongoDB"],
        "contato": "recruta@techsolutions.com.br"
    },
    {
        "id": "2",
        "data_publicacao": "08/04/2025",
        "titulo": "Engenheiro de Machine Learning",
        "empresa": "DataInova",
        "salario": "R$ 12.000 - R$ 15.000",
        "local": "Remoto",
        "descricao": "Profissional para desenvolver e implementar modelos de machine learning escaláveis",
        "requisitos": ["Python", "TensorFlow", "PyTorch", "Estatística", "AWS"],
        "contato": "carreiras@datainova.com"
    },
    {
        "id": "3",
        "data_publicacao": "05/04/2025",
        "titulo": "DevOps Engineer",
        "empresa": "CloudTech",
        "salario": "R$ 9.000 - R$ 11.000",
        "local": "Rio de Janeiro, RJ (Presencial)",
        "descricao": "Especialista em infraestrutura como código e automação de processos de desenvolvimento",
        "requisitos": ["Docker", "Kubernetes", "AWS", "Jenkins", "Terraform"],
        "contato": "jobs@cloudtech.com.br"
    },
    {
        "id": "4",
        "data_publicacao": "02/04/2025",
        "titulo": "Analista de Segurança da Informação",
        "empresa": "SecureNet",
        "salario": "R$ 7.500 - R$ 9.500",
        "local": "Belo Horizonte, MG (Híbrido)",
        "descricao": "Profissional para implementar e monitorar controles de segurança da informação",
        "requisitos": ["Pentest", "Análise de vulnerabilidades", "ISO 27001", "Firewall", "SIEM"],
        "contato": "recrutamento@securenet.com"
    }
]

ALIVE = "sim"

servico = Flask("vagas_ti")

@servico.get("/")
def get():
    return Response(json.dumps(INFO), mimetype="application/json", status=200)

@servico.get("/info")
def get_info():
    return Response(json.dumps(INFO), mimetype="application/json", status=200)

@servico.get("/alive")
def is_alive():
    return Response(ALIVE, mimetype="text/plain", status=200)

@servico.get("/vagas")
def get_vagas():    
    return Response(json.dumps(VAGAS_TI), mimetype="application/json", status=200)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000, debug=True)