from flask import Flask, Response
import json

VERSAO = "1.0.0"

INFO = {
    "descricao": "Serviço que disponibiliza vagas de emprego na área da Saúde",
    "autor": "Claude",
    "versao": VERSAO
}

VAGAS_SAUDE = [
    {
        "id": "1",
        "data_publicacao": "09/04/2025",
        "titulo": "Enfermeiro(a) UTI",
        "empresa": "Hospital Santa Clara",
        "salario": "R$ 4.500 - R$ 5.500",
        "local": "São Paulo, SP (Presencial)",
        "descricao": "Profissional para atuar na Unidade de Terapia Intensiva adulto, em escala 12x36",
        "requisitos": ["Graduação em Enfermagem", "COREN ativo", "Experiência em UTI", "Pós em Terapia Intensiva"],
        "contato": "rh@santaclara.com.br"
    },
    {
        "id": "2",
        "data_publicacao": "07/04/2025",
        "titulo": "Fisioterapeuta",
        "empresa": "Clínica Reabilitar",
        "salario": "R$ 3.800 - R$ 4.500",
        "local": "Campinas, SP (Presencial)",
        "descricao": "Fisioterapeuta para atendimento em ortopedia e traumatologia",
        "requisitos": ["Graduação em Fisioterapia", "CREFITO ativo", "Especialização em Ortopedia"],
        "contato": "contato@reabilitar.com.br"
    },
    {
        "id": "3",
        "data_publicacao": "05/04/2025",
        "titulo": "Médico(a) Cardiologista",
        "empresa": "Centro Médico Cardiosaúde",
        "salario": "R$ 15.000 - R$ 20.000",
        "local": "Rio de Janeiro, RJ (Híbrido)",
        "descricao": "Médico especialista para atendimento ambulatorial e realização de exames",
        "requisitos": ["Graduação em Medicina", "Residência em Cardiologia", "CRM ativo", "Título de especialista"],
        "contato": "vagas@cardiosaude.com.br"
    },
    {
        "id": "4",
        "data_publicacao": "03/04/2025",
        "titulo": "Técnico(a) em Radiologia",
        "empresa": "Instituto de Diagnóstico por Imagem",
        "salario": "R$ 2.800 - R$ 3.500",
        "local": "Belo Horizonte, MG (Presencial)",
        "descricao": "Técnico para operação de equipamentos de tomografia e ressonância magnética",
        "requisitos": ["Curso Técnico em Radiologia", "CRTR ativo", "Experiência em TC e RM"],
        "contato": "recrutamento@idi.com.br"
    }
]

ALIVE = "sim"

servico = Flask("vagas_saude")

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
    return Response(json.dumps(VAGAS_SAUDE), mimetype="application/json", status=200)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000, debug=True)