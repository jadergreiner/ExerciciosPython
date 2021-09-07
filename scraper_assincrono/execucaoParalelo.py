## importando as funções
from requests import get
from bs4 import BeautifulSoup
from multiprocessing import Pool
from time import time



urls = ['https://mentorama.com.br',
        'https://gremio.net/',
        'https://www.globo.com/',
        'https://www.python.org/',
        'https://pandas.pydata.org/',
        'https://www.anaconda.com/',
        'https://aws.amazon.com/pt/',
        'https://www.djangoproject.com/',
        'https://docs.pytest.org/en/6.2.x/',
        'https://www.botscraper.com/']


inicio = time()
def scraper(url):
    r = get(url)
    tags = BeautifulSoup(r.content, "html5lib")
    titulo = title = tags.find("title")
    print(f"Titulo da pagina || >>  {title.text}")


if __name__ == '__main__':
    print("Iniciando o processamento paralelo... \n")
    p = Pool(20)
    p.map(scraper, urls)
    p.terminate()
    p.join()

    print(f"Tempo total de execução: {abs(int(time() - inicio))}")
