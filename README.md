# development-APIRest-format

This format is for the development of APIRest applications in Django

## Initial setup and configuration

It will explain how the project is configured and how to use it correctly.

- Rename the project: Change the name of the folder *"apipqr"*, by the name of the project of your choice.
- Rename: Using search and replace, replace in all files the one with the word *"apipqr"* by the name of the project.

### development.yml file configuration

Configure the ports to be exposed for both the mariadb service and the django service:


This is the example for the django service before configuring it:

`ports: - "PORT:8000"`.

This is the example for the django service after configuring it:

`ports: - "8001:8000"`.

8001 was put as an example, but you can put the port that best suits the developer's configuration.

#### All ports editable

- Django: `PORT:8000`.
- MariaDB: `PORT:3306`.
- Flower: `PORT:5555`

### setting environment variables
Located in the *".envs"* folder is a sample file called *".mariadb.example"*. With this file we will carry out the following steps:

1. Duplicate the file.
2. Rename the duplicate file to *".mariadb"*.
3. Enter the file and fill in the environment variables.

Located in the *".envs"* folder is a sample file called *".django.example"*. With this file we will carry out the following steps:

1. Duplicate the file.
2. Rename the duplicate file to *".django"*.
3. Enter the file and fill in the environment variables.

#### Environment Variables

### python:

- python -m venv .env
- pip install -r requeriments/developmen.txt

##### .mariadb file:

- MYSQL_USER: Represents the username that will affect only the database.
- MYSQL_PASSWORD: Represents the password of the previous user.
##### .django file:

- CELERY_FLOWER_USER: Represents the celery administrator user.
- CELERY_FLOWER_PASSWORD: Represents the celery administrator password.
- DJANGO_SECRET_KEY: Represents the secret password for the django encryptor.

### Create new django apps

With the folder called *"nombreapp"* it is a basic format that allows you to create django applications, the only thing you have to do is:

1. Rename the folder to the name of the application.
2. Using search and replace in all the files in the folder the word *"nombreapp"* with the name of the application.

as a second option is to create a virtual python environment and install the packages that are in the file *"development.txt"* located in the *"requirements"* folder. after that run the following command:

`django-admin startapp [name app]`.

> All applications are saved in the folder named project.

## Docker commands

Basic commands for handling the format through docker:

1. Build images: `docker-compose -f development.yml build`.
2. Start image: `docker-compose -f development.yml up`.
3. Finish image: `docker-compose -f development.yml down`.

Special commands for the python command execution inside the container:

1. Run command: `docker-compose -f development.yml run django [command]`.

Process if you want to have the django console separately:

1. Remove container from django: `docker rm -f [name or id container]`.
2. Start the container in another console: `docker-compose -f development.yml run --rm --service-ports django`.

> Note: By creating this environment variable *"COMPOSE_FILE"* you can omit typing *"-f [name file compose]"*.



Glosario
ORM: Object-relational mapping. Es el encargado de permitir
el acceso y control de una base de datos relacional a través de
una abstracción a clases y objetos.

Templates: Archivos HTML que permiten la inclusión y ejecución
de lógica especial para la presentación de datos.

Modelo: Parte de un proyecto de Django que se encarga de estructurar
las tablas y propiedades de la base de datos a través de clases de Python.

Vista: Parte de un proyecto de Django que se encarga de la
lógica de negocio y es la conexión entre el template y el modelo.

App: Conjunto de código que se encarga de resolver una parte
muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

Patrón de diseño: Solución común a un problema particular.



docker-compose run --rm django python manage.py createsuperuser

docker-compose -f developer.yml run --rm --service-port django
# pqr
