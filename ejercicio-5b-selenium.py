from selenium import webdriver
from bs4 import BeautifulSoup


# Ejemplo b: llenamos un formulario de búsqueda y hacemos clic en buscar:

# Iniciamos el driver y vamos a la página
driver = webdriver.Firefox()
driver.get("https://www.memoriachilena.gob.cl")

# Guardamos en variables los elementos con que nos interesa interactuar
barra_busqueda = driver.find_element("id", "keywords")
boton_busqueda = driver.find_element("id", "boton_busqueda")

# Enviamos información a la barra de búsqueda y luego hacemos clic

barra_busqueda.send_keys("tipografía en Chile")
boton_busqueda.click()

# Extraemos el código fuente de la página

codigo_fuente = driver.page_source

# Cerramos el driver porque ya no lo necesitamos más

driver.quit()

# Creamos la sopa con Beautiful Soup

soup = BeautifulSoup(codigo_fuente, "html.parser")

# Y luego buscamos las cosas que nos interesa buscar


