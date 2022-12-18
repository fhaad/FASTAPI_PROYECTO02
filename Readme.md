![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

### PROYECTO INDIVIDUAL 01 - DATA ENGINEER

### JOSE FEDERICO HAAD ATUESTA - DTS-05

### TABLA GENERAL

1. Introduccion
2. Procedimientos
3. Limpieza ETL (Extract, Transform, Load)
4. Resultado
5. Herramientas utilizadas
6. FastApi (ejecucion)
7. Docker (container)
8. Deploy (Mogenius)
9. Video Tutorial del Proyecto


### 1. INTRODUCCION

En el mundo de DATA la informacion puede llegar de diferentes fuentes y en diferentes estados. Dentro de estas fuentes estan las aplicaciones moviles o web, la red de internet, el internet de las cosas, imagenes y videos. Si magnificamos las fuentes de informacion como se menciona, se podran imaginar la cantidad de pentabytes de informacion lista para ser analizada. Pero antes de esto imaginemos que la DATA no llega estruturada u organizada, son datos crudos que a simple vista no dicen nada. Y he aqui la importancia de los DATA ENGINEER, quienes son los que realizan un procedimiento llamado ETL; en el que consiste en limpiar y organizar los datos de tal manera que puedan ser manipulados y almacenados en un warehouse(bodega de datos) para su futuro procesamiento.

### 2. PROCEDIMIENTOS

Despues de conocer la fuente de los datos y extraerlos se realiza un EDA (Exploratory Data Analysis) o Analisis exploratorio de los datos e identificar las variables y su contenido.
Podemos realizar los siguientes pasos

- Analisis exploratorio
- Documentacion de lo encontrado
- Documentacion de las soluciones
- Impacto del ETL y las necesidades
- Organizacion de la Data 

Dentro del desarrollo de DATA ENGINNER los pasos del analisis son fundamentales y el pre ambulo del trabajo que se debe realizar con la informacion para obtener un buen resultado.


<img src="/src/ETL.jpg"  height="400">

### 3. LIMPIEZA ETL

El proceso de ETL comienza con la extraccion de los datos de forma cruda. Estos archivos originales de los datos se guardaron en un directorio.

DIRECTORIO  ..\DATASET_RAW (Archivos originales)

Se procedió a cargar la data en un DataFrame de pandas para su mejor manipulacion.
Los archivos cargados son de tipo .CSV y .JSON, para un total de 4 archivos con diferente cantidad de columnas y filas.

A continuacion se procede a realizar un EDA con los datos:

Para este procedimiento se utilizo una libreria practica y agil conocida como **pandas-profiling**, que genera un reporte detallado y completo de los datos crudos.

- from pandas_profiling import ProfileReport (Libreria de Reporte): genera un reporte con una interface en HTML.
- Se procedio a guardar estos reportes en un directorio como documentacion encontrada 
DIRECTORIO  ..\EDA_REPORT (Reportes)

- dataset_amazon.html
- dataset_disney.html
- dataset_hulu.html
- dataset_netflix.html

<img src="/src/profiling.jpg"  height="400">

Despues del anterior analisis se procede a aplicar una serie de codigos de limpieza de datos. 
Para cada archivo de DATA se creo un **Jupyter Notebook** con los siguientes nombres

- Carga_dataset_amazon_ETL
- Carga_dataset_disney_ETL
- Carga_dataset_hulu_ETL
- Carga_dataset_netflix_ETL

estos archivos quedaron en el directorio raiz.

Pasos que se aplicaron de limpieza

- Eliminacion de columnas (no necesarias)
- Completar datos faltantes (valores que no afectan el resultado)
- Agregacion de nuevas columnas
- Separacion de datos string y numericos
- Cambio de datos string a numerico
- Verificación de numero de columnas (concatenancion)  

### 4. RESULTADO

Despues de haber aplicado el ETL a cada uno de los archivos de datos se procedio a guardar el resultado de limpieza en achivos tipo .CSV con un nuevo nombre y en un directorio con los siguietes nombres:

DIRECTORIO  ..\DATASET_CLEAN

- dataset_amazon_clean
- dataset_disney_clean
- dataset_hulu_clean
- dataset_netflix_clean

por ultimo se hizo un concatenacion (union) de los archivos limpios en un solo dataset con el siguiente nombre:

- dataset_new

Este archivo dataset_new se pasa a una base de datos **sqlite** para ser utilizado en FastApi. Directorio guardado.

DIRECTORIO  ..\BaseDatos

- dataset_new.db 

<img src="/src/MySQL.jpg"  height="200">

### 5. HERRAMIENTAS UTILIZADAS

estas son las diferentes herramientas y librerias utilizadas

- Visual Studio Code
- Lenguaje de Programacion Python
- Libreria Pandas
- Libreria Pandas-Profiling
- Libreria Sqlalchemy
- Libreria Sqllite

<img src="/src/python.jpg"  height="200">  <img src="/src/alchemy.jpg"  height="200">

### 6. FASTAPI

Es un framework para crear APIs tales como REST APIs o APIs RPC con un rendimiento excelente, para soportar sitios web de alta concurrencia.
FastAPI es totalmente compatible con el tipado y el asincrónismo de las últimas versiones de Python por lo que se hace necesario para este proyecto que nos recrea un entorno laboral en demanda.

estos son los pasos que se realizaron:

- Se instala ambiente virtual (venv)
- Se instala Libreria Pandas
- Se instala Libreria FastApi
- Se instala Libreria Sqlalchemy
- Se instala Uvicorn

Luego se crea un archivo .PY que contendra la conexion a la base de datos

<img src="/src/fastapi.jpg"  height="200">

### 7. DOCKER

Docker es una plataforma diseñada para ayudar a los desarrolladores a crear, compartir y ejecutar aplicaciones. 

Utiliza contenedores, y lo que hacen es reutilizar el kernel, que es la parte mas profunda del SO de la maquina anfitriona, manejando de forma más óptima recursos que ya están disponibles. Esa containerización, trae consigo las ventajas de ser más liviana, portable, de bajo acoplamiento debido a que los contenedores son autocontenidos (no afecta a los demás para su funcionamiento), escalable y segura.


<img src="/src/docker.jpg"  height="200">

### 8. DEPLOY - MOGENIUS

ENLACE: https://fastapi-proyec-prod-proyecto-01-fede-a0vzhm.mo5.mogenius.io/docs

Mogenius es una plataforma en la nube donde puedes alojar tus aplicaciones.  Es aqui donde se hara la ejecucion de nuestra aplicacion enlazada directamente al repositorio de github donde se encuentra todo el desarrollo.


<img src="/src/mogenius.jpg"  height="200">


### 9. VIDEO TUTORIAL

Aqui podra observar un video tutorial de este proyecto.

Enlace: https://youtu.be/X_HzXqmFXgM


### DIAGRAMA DE PROCESO

<img src="/src/Proyecto_01_FastApi_Fede.jpg"  height="600">