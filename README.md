# libgen_parser_downloader

Brach basada en [libgenparser](https://pypi.org/project/libgenparser/) para descargar libros desde Library Genesis en modo batch.

Por default, el script recibe como input una lista de autores, y a partir de allí el programa se encarga de conseguir la metadata de cada libro del autor, generar links de descarga y finalmente descargar los contenidos en un directorio local.

- El directorio local crea una carpeta principal (_download+timestamp_) con una subfolder por autor.
- Dentro de cada subfolder se encuentran los libros descargados, en formato _pdf_, _epub_ y _mobi_

## TODO list
- Testear parser para una lista de autores
- Configurar filtros de lenguaje y extension
- Parsear resultados para no repetir libros para un mismo lenguaje y extension de archivo
- Configurar output de directorio local en folder y subfolders
- Investigar la mejor manera de armar una lista de autores
- Armar lista de autores
- Correr para lista real de autores




## Referencias
- [libgen-api](https://github.com/harrison-broadbent/libgen-api)
- [bardapi](https://pypi.org/project/bardapi/)