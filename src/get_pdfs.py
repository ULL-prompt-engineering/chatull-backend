import requests
import os
import time

# Función que recibe una cadena en snake_case y la convierte a camelCase
def to_camel_case(s):
    words = s.split('_')
    return ''.join([word.capitalize() + '_' for word in words])[0:-1]

# Función que recibe un archivo de texto con enlaces y descarga los pdfs de esos enlaces
def get_pdfs(desde_enlaces_txt):
    if not os.path.exists('pdfs'):
        os.makedirs('pdfs')

    with open(desde_enlaces_txt, 'r') as archivo:
        enlaces = [linea.strip() for linea in archivo]
    contador = 1

    for enlace in enlaces:
        try:
            respuesta = requests.get(enlace)
            
            orig_filename = respuesta.headers['Content-Disposition'].split('=')[1].replace("%20", "_")
            subject_code = orig_filename.split('_')[2]
            filename = orig_filename.split('-')[1][1:-1]
            filename = to_camel_case(filename)
            filename = subject_code + "-" + filename

            nombre_archivo = 'pdfs/' + filename + '.pdf'

            with open(nombre_archivo, 'wb') as archivo_pdf:
                archivo_pdf.write(respuesta.content)

        except Exception as e:
            print(f"Error al descargar desde {enlace}: {e}")
        
        finally:
            contador += 1
            # delay para evitar errores de conexión
            if contador % 5 == 0:
                time.sleep(3)

if __name__ == "__main__":

    archivo_enlaces = "urls.txt"


    get_pdfs(archivo_enlaces)
