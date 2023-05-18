"""
📚 Livro Goalkicker Downloader 📚

Este script foi criado por Diego Queiroz (Diegiwg) com o objetivo de fazer o download de todos os livros gratuitos disponíveis no site books.goalkicker.com. 

Certifique-se de ter as bibliotecas `requests` e `beautifulsoup4` instaladas. Caso não as tenha, você pode instalá-las executando o seguinte comando no terminal:

    pip install -r requirements.txt

🚀 Como usar:
    1. Execute o script em seu ambiente Python.
    2. Aguarde enquanto o script faz a solicitação e o processamento dos livros disponíveis no site.
    3. Os livros serão baixados e salvos em um diretório chamado 'Livros Goalkicker' na mesma pasta onde o script está sendo executado.

⚠️ Aviso:
    - Este script foi desenvolvido apenas para fins educacionais e de aprendizado.
    - Certifique-se de que você tem permissão para baixar e usar os livros disponíveis no site books.goalkicker.com.
    - Respeite os direitos autorais e os termos de uso de cada livro.

📖 Aproveite a leitura e bons estudos!

"""

import os
import requests
from bs4 import BeautifulSoup


URL = "https://books.goalkicker.com/"
DIR = f"{__file__.rstrip(os.path.basename(__file__))}/Livros Goalkicker"


def config():
    os.makedirs(DIR, exist_ok=True)


def save_book(title: str, book_blob: bytes):
    print(f"📚 Baixando livro {title}...")
    with open(f"{DIR}/{title}.pdf", "wb") as file:
        file.write(book_blob)


def download_book(book_url: str):
    response = requests.get(f"{URL}{book_url}")
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select_one("h1").get_text(strip=True)
    down = soup.select_one(".download").get("onclick").split("'")[1].split("'")[0]

    book_blob = requests.get(f"{URL}{book_url}/{down}").content
    save_book(title, book_blob)


def main():
    config()

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.select(".bookContainer a")
    for book in books:
        book_url = book.get("href")
        download_book(book_url)


if __name__ == "__main__":
    main()
