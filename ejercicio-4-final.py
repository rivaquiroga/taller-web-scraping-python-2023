# Taller de web scraping con Python
# Diplomado en Ciencia de Datos UC
# Sesión a cargo de Riva Quiroga (https://rivaquiroga.cl)

# Ejercicio 4: descarga de archivos

import requests
from bs4 import BeautifulSoup
import time

# Paso 1: extraemos los enlaces que nos interesan

sitio = "https://www.memoriachilena.gob.cl/602/w3-article-644324.html#documentos"
respuesta = requests.get(sitio)
contenido = respuesta.text
soup = BeautifulSoup(contenido, "html.parser")

# Nos enfocamos solo en la sección de artículos

seccion_articulos = soup.find("div", id = "recuadros_articulo_683_group_pvid_147059")
len(seccion_articulos)

# Y de ahí extraemos los recuadros en que está la información de cada uno de los documentos. 
recuadros = seccion_articulos.find_all("div")

# Ahora, iteramos sobre la lista que creamos y dentro de el elemento "p" buscamos el elemento "a".
enlaces_pdf = []
for recuadro in recuadros:
    enlace = recuadro.find("p", class_ = "vermas").a.get("href")
    enlaces_pdf.append(enlace)


# Paso 2: iteramos sobre nuestra lista de enlaces y descargamos cada uno de los archivos. 

for enlace in enlaces_pdf:
    try:
        time.sleep(2)
        nombre_archivo = enlace.split("/")[-1]
        ruta_destino = f"datos-extraidos/{nombre_archivo}"
        respuesta = requests.get(enlace)
        archivo = open(ruta_destino, "wb")
        archivo.write(respuesta.content)
        archivo.close()
        print(f"El archivo {nombre_archivo} ha sido descargado")
    except:
        print(f"El enlace {enlace} no funcionó y no se pudo completar la descarga")