# Web scraping con Python

En este módulo del [Diplomado en Ciencia de Datos UC](https://datascience.uc.cl/) aprenderemos a implementar la técnica de extracción de datos conocida como _web scraping_ usando la librería Beautiful Soup. Las sesiones serán en modalidad online, los días 10 y 17 de junio. 

## Preparación

Para realizar las actividades planificadas necesitarás las librerías `request`, `beautifulsoup4` y `pandas`. Se pueden instalar desde [PyPI](https://pypi.org/) con `pip`. 

```
pip install beautifulsoup4
pip install requests
pip install pandas
pip install lxml
```

Si prefieres trabajar en Google Colab, no olvides agregar un signo de exclamación al inicio de cada línea para su instalación, es decir:

```
!pip install beautifulsoup4
!pip install requests
!pip install pandas
!pip install lxml
```
Esto le indica a Google Colab que ese no es código de Python, sino código que tiene que ejecutarse en la Terminal.

Si trabajas en Visual Studio Code, es necesario que crees un entorno virtual. Durante la primera clase mostraremos cómo hacerlo. También puedes revisar [las indicaciones en este documento](https://github.com/rivaquiroga/taller-web-scraping-python-2023/blob/main/crear-entorno-virtual.md).


## Atajos de teclado útiles

Los siguientes atajos de teclado serán útiles al explorar las páginas web que _escrapearemos_.

| Acción | Windows / Linux | Mac |
|---|---|---|
| Ver el código fuente | ctrl +  u | command + u|
| Abrir el panel de desarrollo | F12<br/>ctrl + shift + i | F12<br/>option + command +i |
| Abrir el panel de desarrollo con la opción de selección activada | ctrl + shift + c | option/ctrl + command + c |


## Enlaces ejemplos

A lo largo de la sesión revisaremos algunos sitios web a modo de ejemplo o para discutir algunas ideas. Los compartiremos por el chat de Zoom y quedarán acá también como referencia.

:link: [Sitio web estático](https://datascience.uc.cl/que-es-ciencia-de-datos)

:link: [Sitio web dinámico](https://www.camara.cl/transparencia/asesoriasexternasgral.aspx)

:link: [Condiciones de uso](https://www.amazon.com/-/es/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou) 

:link: [Licenciamiento y uso del contenido 1](http://programminghistorian.org/es/)

:link: [Licenciamiento y uso del contenido 2](https://prensa.presidencia.cl/)

:link: [robots.txt](https://www.memoriachilena.gob.cl/robots.txt)

## Actividades

Durante las dos sesiones del módulo realizaremos una serie de actividades para poner en práctica lo aprendido. Iremos escribiendo el código "en vivo" en la clase, por lo que el contenido de los archivos con código se irá actualizando a medida que escribamos en ellos. 

### Ejercicio 1: extraer datos de un sitio "mínimo"

:link: [Página web](https://rivaquiroga.github.io/taller-web-scraping-python-2023/ejercicio-1.html)

:page_facing_up: [Código escrito en clases](https://www.dropbox.com/s/uhxmzj8uuamq9xz/ejercicio-1.py?dl=0)

:sparkles: [Versión final del código](https://github.com/rivaquiroga/taller-web-scraping-python-2023/blob/main/ejercicio-1-final.py)

### Ejercicio 2: el mismo ejercicio, pero ahora en un sitio de verdad

:link: [Página web](http://programminghistorian.org/es/lecciones/)

:page_facing_up: [Código escrito en clases](https://www.dropbox.com/s/xuy2l9cs6j9rnq6/ejercicio-2.py?dl=0)

:sparkles: [Versión final del código](https://github.com/rivaquiroga/taller-web-scraping-python-2023/blob/main/ejercicio-2-final.py)

### Ejercicio 3: extraer tablas

:link: [Página web ejemplo 1](https://www.worldometers.info/world-population/population-by-country/) / [Página web ejemplo 2](https://es.wikipedia.org/wiki/Anexo:%C3%81lbumes_musicales_m%C3%A1s_vendidos)

:page_facing_up: [Código escrito en clases](https://www.dropbox.com/s/i48a6dxqiafk7dg/ejercicio-3.py?dl=0)

### Ejercicio 4: descargar archivos a partir de enlaces extraídos

:link: [Página web](https://www.memoriachilena.gob.cl/602/w3-article-644324.html#documentos)

:page_facing_up: [Código escrito en clases](https://www.dropbox.com/s/hf9tg7acq53gp41/ejercicio-4.py?dl=0)

:desktop_computer: [Video sobre uso de try/except en nuestro código de descarga](https://vimeo.com/837228532/5b37603e4d)

:sparkles: [Versión final del código](https://github.com/rivaquiroga/taller-web-scraping-python-2023/blob/main/ejercicio-4-final.py)

### Ejercicio 5: demo selenium

:link: [Página web ejemplo a](https://www.camara.cl/transparencia/oficinasparlamentarias.aspx) / [Página web ejemplo b](https://www.memoriachilena.gob.cl)

:page_facing_up: [Código ejemplo a](https://github.com/rivaquiroga/taller-web-scraping-python-2023/blob/main/ejercicio-5a-selenium.py) / [Código ejemplo b](https://github.com/rivaquiroga/taller-web-scraping-python-2023/blob/main/ejercicio-5b-selenium.py)

## Recursos adicionales

### Documentación librerías utilizadas
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Selenium](https://www.selenium.dev/documentation/)
