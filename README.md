# ai-book-downloader

## Concepto
La búsqueda de libros en Internet suele ser un trabajo tedioso. En especial, cuando no se conocen los autores o títulos de libros más relevantes a la hora de aprender sobre un tópico en general, este proceso de búsqueda manual suele demandar mucho tiempo.

Este es un programa para automatizar dicha búsqueda y descarga de libros. Seleccionando un tópico genérico que se desee aprender (ejemplo: macroeconomía, soap operas del siglo XXI, filosofía antigua, etc.), se genera a través de inteligencia artificial una lista de libros más relevantes. Posteriormente, dichos libros son automáticamente descargados usando la API de Libgen, y consolidados en una carpeta de descargas en el directorio local.

El codigo contiene 3 partes:
1. *Consulta a AI*: conexion a _Bard API_ y extracción de respuesta como diccionario de Python
2. *Obtencion de links*: conexión a _Libgen API_ para obtención de links de descarga
3. *Descarga de archivos*: uso de librería _urllib_ para nombrar archivos y consolidar resultados en una carpeta dentro del directorio local.

El manejo de inteligencia artificial está basado en [bardapi](https://pypi.org/project/bardapi/), el cual utiliza la _API de Google Bard_ para realizar una consulta personalizada. El resultado otorgado por la AI es luego parseado y convertido en mirrors de descarga de Libgen.

El código de Libgen está basado en [libgen_api](https://github.com/harrison-broadbent/libgen-api), con una modificación sobre el código fuente para posibilitar búsquedas holísticas (tanto autor como título dentro de la misma búsqueda).

## INPUTS DE USUARIO
1. limite de libros
2. consulta a Bard

## OUTPUT
El resultado final es una carpeta en el directorio local con los contenidos descargados.

## TODO LIST
1. Usar la libreria click para armar el cli
2. Automatizar el proceso de recoleccion de token de Bard
3. sumar la funcionalidad de descarga en mas de un tipo de extension (epub o mobi)
4. guardar resultados en forma de directorios con subcarpetas según tipo de extensión

## Referencias
- [libgen-api](https://github.com/harrison-broadbent/libgen-api)
- [bardapi](https://pypi.org/project/bardapi/)