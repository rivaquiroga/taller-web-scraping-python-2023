from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd 

# Ejemplo a: seleccionamos un valor de un menú desplegable

# Creamos el driver
driver = webdriver.Firefox()

# Vamos a la página que nos interesa
driver.get("https://www.camara.cl/transparencia/oficinasparlamentarias.aspx")

# Creamos una variable con el elemento con el que queremos interactuar
menu_mes = driver.find_element("id", "ContentPlaceHolder1_ContentPlaceHolder1_ddlMes")


# Esta línea es solo para que vean que el robot hace las cosas que le decimos
menu_mes.click()

# Ahora, volvamos al menú que nos interesa. Primero, lo seleccionarom

Select(menu_mes).select_by_visible_text("enero")


# Luego de esto hay dos opciones:
# 1. Seguimos trabajando con selenium y las funciones y métodos que tiene la librería para extraer los datos que nos interesan. 
# 2. Guardamos todo el código fuente en una variable y trabajamos desde ahí con lo que ya sabemos de Beutiful Soup o con pandas si es una tabla (como acá). Ilustraremos esta segunda opción:

# Extremos el código fuente de la página que tenemos abierta

codigo_fuente = driver.page_source

# Desde este punto ya no necesitamos el driver, así que lo cerramos:

driver.quit()

# Y ahora seguimos trabajando con lo que ya sabemos. Por ejemplo, que para extraer una tabla usamos read_html:


tabla_enero = pd.read_html(codigo_fuente)

