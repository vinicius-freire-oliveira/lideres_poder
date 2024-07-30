import requests
from bs4 import BeautifulSoup
import csv

# URL da página da Wikipedia
url = 'https://pt.wikipedia.org/wiki/Lista_de_l%C3%ADderes_n%C3%A3o_monarcas_que_governaram_por_mais_tempo'

# Fazer a requisição HTTP para a página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todas as tabelas na página
tables = soup.find_all('table', class_='wikitable')

# Nome do arquivo CSV onde os dados serão salvos
csv_file = 'lideres_nao_monarcas.csv'

# Abrir o arquivo CSV para escrita
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Iterar sobre cada tabela e extrair os dados
    for table in tables:
        # Encontrar o cabeçalho da tabela
        headers = [header.text.strip() for header in table.find_all('th')]

        # Escrever o cabeçalho no CSV
        writer.writerow(headers)
        
        # Iterar sobre cada linha da tabela
        for row in table.find_all('tr')[1:]:  # Ignorar a primeira linha que é o cabeçalho
            cells = row.find_all('td')
            
            # Garantir que todos os dados sejam extraídos
            data = [cell.text.strip() for cell in cells]
            
            # Adicionar uma verificação para garantir que as linhas tenham o mesmo número de células que os cabeçalhos
            if len(data) == len(headers):
                writer.writerow(data)  # Escrever os dados no CSV

print(f'Dados foram salvos no arquivo {csv_file}')
