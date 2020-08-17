import requests
from bs4 import BeautifulSoup

url = ('https://cnpj.biz/empresas')

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')
lista_title = soup.find_all('h2')
#lista_title = soup.find_all('title')
print('Lista de empresas: ')
for lista_dados in lista_title:
    print(lista_dados.next_element)
    print('=' * 55)