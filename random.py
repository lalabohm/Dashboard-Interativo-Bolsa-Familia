import csv
import random
from faker import Faker

fake = Faker('pt_BR')

# Função para gerar dados aleatórios para Bolsa Família
def gerar_dados_bolsa_familia(quantidade):
    dados = [["ID", "Nome", "Valor", "Mês", "Ano"]]
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio",
        "Junho", "Julho", "Agosto", "Setembro", "Outubro",
        "Novembro", "Dezembro"
    ]
    for i in range(1, quantidade + 1):
        nome = fake.name()
        mes = random.choice(meses)
        ano = random.randint(2019, 2024)
        dados.append([i, nome, valor, mes, ano])
    return dados

def gerar_dados_regionais(quantidade):
    dados = [["Região", "População", "PIB", "Taxa Desemprego", "Ano"]]
    regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
    for _ in range(quantidade):
        regiao = random.choice(regioes)
        populacao = random.randint(100000, 5000000)
        pib = round(random.uniform(10000, 50000), 2)  # PIB em milhares
        taxa_desemprego = round(random.uniform(3, 15), 2)  # Taxa entre 3% e 15%
        ano = random.randint(2019, 2024)
        dados.append([regiao, populacao, pib, taxa_desemprego, ano])
    return dados

def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

dados_bolsa_familia = gerar_dados_bolsa_familia(100)  # 100 registros
salvar_csv("bolsa_familia_aleatorio.csv", dados_bolsa_familia)

dados_regionais = gerar_dados_regionais(50)  # 50 registros
salvar_csv("dados_regionais_aleatorio.csv", dados_regionais)

print("Arquivos CSV gerados com sucesso!")
