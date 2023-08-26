# libgen_parser_downloader

Brach basada en [libgenparser](https://pypi.org/project/libgenparser/) para **scrapear y descargar libros desde Library Genesis en modo batch**.

El script recibe un _nombre de autor como input_, así como una _carpeta de destino para las descargas_, y a partir de allí el programa se encarga de conseguir la metadata de cada libro del autor, generar links de descarga y finalmente descargar los contenidos en un directorio local.

A su vez, se ha añadido un **análisis de lógica difusa** (basada en la distancia Levenshtein) para:
- _Evitar descargar libros duplicados_. Los archivos que posean misma extensión y lenguaje son sometidos a un fuzzy search, conservando ejemplares únicos, sin repetición.

- _Limpieza de directorio local en base a nombres de autor_. Esto es debido a que, en ocasiones, el autor es el mismo a pesar de mostrarse de diversas maneras en la base de datos (ej: 'Marcus Aurelius', 'Marco Aurelio', 'Emperor of Rome Marcus Aurelius', etc.). De esta manera, en caso de encontrar un duplicado, las carpetas son fusionadas, optimizando la limpieza del directorio de carpetas final.

## Instrucciones
- Clonar el repo del presente branch (libgen_parser_downloader)
```bash
git clone -b libgen_parser_downloader git@github.com:JuanMartinElorriaga/libgen_parser_downloader.git
```
- Dirigirse al root folder del repo
- Instalar las dependencias necesarias con la terminal:
```bash
pipenv shell
pipenv install
```
- Correr el `CLI`, indicando el autor a descargar. Esto puede hacerse tanto con el flag `--author` como luego de correr la siguiente sentencia:
```python
python3 libgen_parser_downloader
```
- En caso de dejar la carpeta de destino por default, se escogerá la carpeta `downloads` en el mismo nivel que el script. En caso de no existir, será creada automáticamente.

## Referencias
- [bardapi](https://pypi.org/project/bardapi/)
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
- [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [libgen-api](https://github.com/harrison-broadbent/libgen-api)
- [libgenparser](https://pypi.org/project/libgenparser/)