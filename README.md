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

:desktop_computer: [Página web](https://rivaquiroga.github.io/taller-web-scraping-python-2023/ejercicio-1.html)

:page_facing_up: [Código escrito en clases](https://www.dropbox.com/s/uhxmzj8uuamq9xz/ejercicio-1.py?dl=0)

:sparkles: Versión final del código (pronto)

### Ejercicio 2: el mismo ejercicio, pero ahora en un sitio de verdad

:desktop_computer: [Página web](http://programminghistorian.org/es/lecciones/)

:page_facing_up: [Código escrito en clases](https://www.dropbox.com/s/xuy2l9cs6j9rnq6/ejercicio-2.py?dl=0)

:sparkles: Versión final del código (pronto)

### Ejercicio 3: extraer tablas

:desktop_computer: Página web

:page_facing_up: Código escrito en clases

### Ejercicio 4: descargar archivos a partir de enlaces extraídos

:desktop_computer: Página web

:page_facing_up: Código escrito en clases

### Ejercicio 5: demo selenium

:desktop_computer: Página web

:page_facing_up: Código

## Recursos adicionales

Acá iremos agregando enlaces a material complementario para que puedan seguir profundizando en este tema en el futuro.

