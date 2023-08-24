# libgen_parser_downloader

Repo basado en [libgenparser](https://pypi.org/project/libgenparser/) para descargar libros desde Library Genesis en modo batch.

Por default, el script recibe como input una lista de autores, y a partir de allí el programa se encarga de conseguir la metadata de cada libro del autor, generar links de descarga y finalmente descargar los contenidos en un directorio local.

- El directorio local crea una carpeta principal (_download+timestamp_) con una subfolder por autor.
- Dentro de cada subfolder se encuentran los libros descargados, en formato pdf, epub y mobi

## Referencias
- [libgen-api](https://github.com/harrison-broadbent/libgen-api)
- [bardapi](https://pypi.org/project/bardapi/)