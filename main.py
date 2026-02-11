import requests
import pandas as pd

# 1. Criando URL e parâmetros da API
url_base = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
rota = 'CotacaoDolarPeriodo'
dataInicial = '01-01-2020'
dataFinalCotacao = '12-31-2030'
top = 10000
format = 'json'

url = f"{url_base}{rota}(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{dataInicial}'&@dataFinalCotacao='{dataFinalCotacao}'&$top={top}&$format={format}"

# 2. Acessando e Requisitando a API
r = requests.get(url)
dados = r.json()

# 3. Criar DataFrame e criar planilha em Excel
df = pd.DataFrame(dados['value'])
df.to_excel('Histórico_Dolar.xlsx')

print('Arquivo gerado com sucesso!')
