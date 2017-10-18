# telegram-respobot

## Synopsis

Bot de **telegram** escrito en **python** para responder a preguntas frecuentes de los hermanos de la comunidad 13 de las santas de Barcelona. 

## Motivation

Aprender a utilizar la API de **telegram** y desplegar en **heroku**.

## Installation

### Preparar el entorno

$ pip install virtualenv

$ mkdir project_dir

$cd project_dir 

$ virtualenv my_env

$ cd my_env

### Descargar el código 

$ git clone https://github.com/24ndres/telegram-respobot

$ cd ..

### Activar virtualenv

$ source bin/activate

$ git init

### Necesario para hacer deploy en heroku

$ git add .

$ git commit -m 'Mensaje del commit'

$ heroku login

$ heroku create

$ git push heroku master

$ heroku ps:scale bot=1

$ heroku logs --tail
