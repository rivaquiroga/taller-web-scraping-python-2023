import requests 
from bs4 import BeautifulSoup
import pandas as pd

# 1. Hacemos la solicitud de información y creamos la "sopa"
sitio = "http://programminghistorian.org/es/lecciones/"
respuesta = requests.get(sitio)
contenido = respuesta.text
soup = BeautifulSoup(contenido, "html.parser")

# 2. Extraemos los datos que nos interesan

# recorte de la zona de la página que nos interesa:

lista_lecciones = soup.find_all("div", class_ = "lesson-description")

# creamos las listas vacías que van a recibir los datos

titulos = []
autores = []
resumenes = []
enlaces = []
fechas = []
topicos = []
actividades = []
dificultades = []

# Iteramos sobre listas_lecciones: extraemos los datos que nos interesan y los guardamos en la lista correspondiente. Acá lo hicimos en un solo paso en cada caso, es decir, no creamos una variable intermedia a la que luego le hicimos append, sino que hicimos todo de una sola vez. En ambos casos el resultado es el mismo.

for leccion in lista_lecciones:
    titulos.append(leccion.h2.get_text(strip = True))
    autores.append(leccion.h3.get_text(strip = True))
    resumenes.append(leccion.p.get_text(strip = True))
    enlace = leccion.a.get("href")
    enlaces.append(f"http://programminghistorian.org{enlace}")
    fechas.append(leccion.find("span", class_ = "date").get_text())
    topicos.append(leccion.find("span", class_ = "topics").get_text().split())
    actividades.append(leccion.find("span", class_ = "activity").get_text())
    dificultades.append(leccion.find("span", class_ = "difficulty").get_text())


# 3. Transformamos estos datos a la estructura de datos que nos interesa: un data frame

# juntamos todo en un dicionario
lecciones = {"titulo": titulos, "autores": autores, "resumen": resumenes, "enlace": enlaces, "fecha_publicacion": fechas, "topicos": topicos, "actividad": actividades, "dificultad": dificultades}

# convertimos a data frame y ajustamos la columna dificultad para que sea numérica (quedó como caracter)

df_lecciones = pd.DataFrame(lecciones)

df_lecciones["dificultad"] = df_lecciones["dificultad"].astype(int)

# 4. Guardamos una copia local en formato CSV

df_lecciones.to_csv("lecciones-ph_es.csv", index = False)
