# **Dashboard Interativo - Bolsa Família e Dados Regionais**

Este é um projeto desenvolvido com **Streamlit**, que apresenta um dashboard interativo para análise de dados relacionados ao programa Bolsa Família e dados regionais contextuais. O objetivo é mesclar, filtrar e visualizar informações de dois conjuntos de dados (CSV e banco de dados MySQL) de maneira eficiente e amigável.

---

## **Objetivo do Projeto**

O dashboard oferece:

1. **Visualização dos Dados**:
   - Informações sobre beneficiários do Bolsa Família (idade, benefício, filhos, carro, etc.).
   - Dados regionais (município, IDH).
2. **Filtros Interativos**:
   - Filtrar por município, faixa de idade e valor mínimo de benefício.
3. **Exportação**:
   - Baixar dados filtrados diretamente em formato CSV.
4. **Estatísticas Descritivas**:
   - Resumo estatístico dos dados.
5. **Conexão com Banco de Dados**:
   - Integração com MySQL para consulta e atualização dos dados em tempo real.

---

## **Estrutura dos Arquivos**

| Arquivo                           | Descrição                                                             |
| --------------------------------- | --------------------------------------------------------------------- |
| `csv_streamlit.py`                          | Código principal do projeto, implementado em **Streamlit**.           
| `bolsa_familia_hypotetico.csv`    | Dados fictícios do Bolsa Família (idade, município, benefício, etc.). |
| `dados_regionais_contextuais.csv` | Dados regionais (município, IDH).                                     
                    

## **Estrutura do Dashboard**

O dashboard possui três abas principais:

### **1. Dados Combinados**
- Mescla os dados do Bolsa Família com os dados regionais pelo município.
- Filtros interativos:
  - Município.
  - Faixa de idade.
  - Valor mínimo do benefício.
- Exportação de dados filtrados em formato CSV.

### **2. Bolsa Família**
- Exibição dos dados originais do programa Bolsa Família.
- Estatísticas descritivas:
  - Média.
  - Mínimo.
  - Máximo.
  - Outras informações estatísticas relevantes.

### **3. Dados Regionais**
- Exibição dos dados regionais (IDH por município).
- Estatísticas descritivas:
  - Média.
  - Mínimo.
  - Máximo.
  - Outras informações estatísticas relevantes.
---

## **Como Executar o Projeto**

### **Pré-requisitos**

1. Ter o Python instalado (versão >= 3.8).
2. Instalar o **Streamlit** e outras dependências listadas em `requirements.txt`.
3. Ter um banco de dados MySQL configurado com os dados necessários.

### **Instalação**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/dashboard-bolsa-familia.git
   cd dashboard-bolsa-familia
   ```

## **Instale as Dependências**

````bash
pip install -r requirements.txt

## **Configure a Conexão com o MySQL no Arquivo `app.py`**

```python
import mysql.connector

connection = mysql.connector.connect(
    host='seu_host',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
````
