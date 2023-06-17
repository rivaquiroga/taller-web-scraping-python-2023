import requests 
from bs4 import BeautifulSoup
import pandas as pd

# 1. Hacemos la solicitud de información y creamos la "sopa"
sitio = "https://rivaquiroga.github.io/taller-web-scraping/ejemplo-1.html"
respuesta = requests.get(respuesta)
contenido = respuesta.text
soup = BeautifulSoup(contenido, "html.parser")

# 2. Extraemos los datos que nos interesan

# Buscamos los encabezados
elementos_h2 = soup.find_all("h2") 

# Iteramos sobre la variable que creamos y guardamos el texto de los encabezados en una lista
librerias = []
for elemento in elementos_h2:
    librerias.append(elemento.get_text())

# Hacemos lo mismo con las descripciones
elementos_p = soup.find_all("p", class_ = "librerias")

descripcion = []
for elemento in elementos_p:
    descripcion.append(elemento.get_text())
    
# Y con los enlaces
elementos_a = soup.find_all("a")

enlaces = []
for elemento in elementos_a:
    enlaces.append(elemento.get("href"))

# 3. Transformamos estos datos a la estructura de datos que nos interesa: un data frame

# Primero creamos un diccionario
web_scraping = {"libreria": librerias, "descripcion": descripcion, "enlace": enlaces}

# Y luego lo convertimos en un data frame
df_librerias = pd.DataFrame(web_scraping)

# 4. Guardamos una copia local en formato CSV

df_librerias.to_csv("datos-extraidos/librerias-web-scraping.csv", index=False)
