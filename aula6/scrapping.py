import requests
from bs4 import BeautifulSoup

# URL da página da UOL
url = "https://www.uol.com.br/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fazendo requisição HTTP
resposta = requests.get(url, headers=headers)

# Verificar se deu certo
if resposta.status_code == 200:
    # Código 200 == sucesso
    print("Requisição feita com sucesso")
    
    # Tratando o HTML
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Encontrando as notícias
    noticias = soup.find_all("a", class_="headlineMain__link")
    
    print("Últimas notícias da UOL: ")
    for index, noticia in enumerate(noticias):
        titulo = noticia.text.strip()
        link = noticia['href']
        print(f"{index+1}. {titulo} - {link}\n")
else:
    print(f"Erro na requisição: {resposta.status_code}")
