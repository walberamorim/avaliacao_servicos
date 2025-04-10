from flask import Flask, Response
import json

VERSAO = "1.0.0"

INFO = {
    "descricao": "Serviço que disponibiliza vagas de emprego na área Comercial",
    "autor": "Claude",
    "versao": VERSAO
}

VAGAS_COMERCIAL = [
    {
        "id": "1",
        "data_publicacao": "10/04/2025",
        "titulo": "Gerente de Vendas",
        "empresa": "BestSell Distribuidora",
        "salario": "R$ 6.000 - R$ 8.000 + comissão",
        "local": "São Paulo, SP (Presencial)",
        "descricao": "Gerenciar equipe de vendas e desenvolver estratégias para atingir metas comerciais",
        "requisitos": ["Experiência em gestão de equipes", "Conhecimento em técnicas de vendas", "Excel avançado"],
        "contato": "talentos@bestsell.com.br"
    },
    {
        "id": "2",
        "data_publicacao": "08/04/2025",
        "titulo": "Consultor(a) de Vendas",
        "empresa": "AutoMax Veículos",
        "salario": "R$ 2.500 + comissão",
        "local": "Florianópolis, SC (Presencial)",
        "descricao": "Realizar atendimento a clientes e venda de veículos novos e seminovos",
        "requisitos": ["Ensino médio completo", "CNH B", "Experiência com vendas", "Boa comunicação"],
        "contato": "rh@automax.com.br"
    },
    {
        "id": "3",
        "data_publicacao": "07/04/2025",
        "titulo": "Analista de Marketing Digital",
        "empresa": "E-Market Solutions",
        "salario": "R$ 4.500 - R$ 5.500",
        "local": "Curitiba, PR (Híbrido)",
        "descricao": "Responsável por campanhas de marketing digital e gestão de mídias sociais",
        "requisitos": ["Experiência com Google Ads", "Meta Ads", "Analytics", "Inbound Marketing"],
        "contato": "oportunidades@emarket.com.br"
    },
    {
        "id": "4",
        "data_publicacao": "04/04/2025",
        "titulo": "Key Account Manager",
        "empresa": "Global Partners",
        "salario": "R$ 7.000 - R$ 9.000 + benefícios",
        "local": "Brasília, DF (Híbrido)",
        "descricao": "Gerenciar relacionamento com contas-chave e desenvolver novos negócios",
        "requisitos": ["Inglês avançado", "Experiência com grandes contas", "Gestão de relacionamento"],
        "contato": "carreiras@globalpartners.com.br"
    }
]

ALIVE = "sim"

servico = Flask("vagas_comercial")

@servico.get("/")
def get():
    return Response(json.dumps(INFO), mimetype="application/json", status=200)

@servico.get("/alive")
def is_alive():
    return Response(ALIVE, mimetype="text/plain", status=200)

@servico.get("/vagas")
def get_vagas():    
    return Response(json.dumps(VAGAS_COMERCIAL), mimetype="application/json", status=200)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000, debug=True)