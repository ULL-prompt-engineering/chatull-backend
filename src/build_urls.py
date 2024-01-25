import requests
from bs4 import BeautifulSoup

def get_urls(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        soup = BeautifulSoup(respuesta.content, 'html.parser')

        enlaces = [enlace['href'] for enlace in soup.find_all('a', href=True)]

        enlaces = ['https://www.ull.es' + enlace.replace('view_guide', 'print_guide') for enlace in enlaces if '/view_guide/' in enlace]
#
        return enlaces
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página: {e}")

if __name__ == "__main__":
    url_a_analizar = 'https://www.ull.es/apps/guias/guias/view_degree/Grado%20en%20Ingenier%C3%ADa%20Inform%C3%A1tica/'
    enlaces_en_pagina = get_urls(url_a_analizar)

    with open('enlaces.txt', 'w') as archivo:
        for enlace in enlaces_en_pagina:
            archivo.write(enlace + '\n')
