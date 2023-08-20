# ai-book-downloader

## Concepto
Este es un programa para automatizar la busqueda y descarga de libros de relevancia,
a partir de las sugerencias dadas por AI y obtencion de contenidos en Libgen.

El codigo contiene 3 partes:
1. *Consulta a AI*: conexion a Bard API y extraccion de respuesta como diccionario de python
2. *Obtencion de links*: conexion a Libgen API para obtencion de links de descarga
3. *Descarga de archivos*: uso de terminal para nombrar archivos y consolidar resultados en una carpeta

## INPUTS DE USUARIO
1. limite de libros
2. consulta a Bard

## OUTPUT
El resultado final es una carpeta en el directorio local con los contenidos descargados

## TODO LIST
1. Usar bard api para generar una consulta
2. Limpiar la respuesta para generar un diccionario de recomendaciones
3. Usar como input el punto 2 para realizar las busquedas de metadata en libgen
4. Usar la metadata del punto 3 para generar los links de descarga
5. Descargar a traves de los links usando la terminal
6. guardar resultados en una carpeta local
    - armar dos subcarpetas: una para pdf y otra para epub o mobi

## ADICIONALES
1. Usar la libreria click para armar todo como un CLI
2. Modificar código de libgen-api para agregar holistic approach que busque tanto autor como titulo de libro


## Referencias
- (libgen-api)[https://github.com/harrison-broadbent/libgen-api]
