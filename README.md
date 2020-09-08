# Tutorial de Flask

Este tutorial tiene como objetivo desarrollar un mini blog usando el framework web Flask, el cuál está basado en Python.

Durante las diferentes lecciones se verá todo aquello que, personalmente, considero que hay que tener en cuenta a la
hora de desarrollar una aplicación web (cualquier aplicación web, no solo en Flask). Por tanto, se repasarán aspectos
esenciales como gestión de usuarios, control de errores, trazas de log, seguridad, test o arquitectura.

Puedes seguir el tutorial en https://j2logo.com/tutorial-flask-espanol/

## Funcionalidades del miniblog

El miniblog a desarrollar tendrá las siguientes características:

* Existirán dos tipos de usuario: administradores e invitados.
* Un usuario administrador puede añadir, modificar y eliminar entradas del blog.
* Los usuarios invitados pueden registrarse en el blog para comentar las diferentes entradas.
* Un usuario administrador puede listar y eliminar usuarios, además de poder asignarles el rol de administrador.

## Lecciones del tutorial

* Lección 1: La primera aplicación Flask
* Lección 2: Uso de plantillas para las páginas HTML
* Lección 3: Uso de formularios en Flask
* Lección 4: Gestión de usuarios: Registro y Login
* Lección 5: Añadiendo una base de datos: SQLAlchemy
* Lección 6: Estructura de un proyecto con Flask: blueprints
* Lección 7: Parámetros de configuración de un proyecto Flask
* Lección 8: Gestión de errores
* Lección 9: Logs en Flask
* Lección 10: Añadiendo seguridad en las vistas
* Lección 11: Actualizar la base de datos SQLAlchemy
* Lección 12: Test con Flask
* Lección 13: Paginar las consultas de base de datos
* Lección 14: Enviar emails con Flask
* Lección 15: Trabajar con Fechas en Flask
* Lección 16: Procesar ficheros en Flask
* Lección 17: Desplegar una aplicación Flask en un entorno de producción

  
## Descarga e instalación del proyecto

Para descargar el proyecto puedes clonar el repositorio:

    git clone https://github.com/j2logo/tutorial-flask.git
    
> Cada una de las lecciones se corresponde con una hoja del repositorio.
> El nombre de las hojas es "leccionXX".

Si quieres descargar una lección en concreto, ejecuta el siguiente comando git:

    git checkout tags/<leccionXX> -b <nombre-de-tu-rama>

Por ejemplo:

    git checkout tags/leccion1 -b leccion1

### Variables de entorno

Para que el miniblog funcione debes crear las siguientes variables de entorno:

#### Linux/Mac

    export FLASK_APP="entrypoint"
    export FLASK_ENV="development"
    export APP_SETTINGS_MODULE="config.local"

#### Windows

    set "FLASK_APP=entrypoint"
    set "FLASK_ENV=development"
    set "APP_SETTINGS_MODULE=config.local"
    
> Mi recomendación para las pruebas es que añadas esas variables en el fichero "activate" o "activate.bat"
> si estás usando virtualenv
 
### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

    pip install -r requirements.txt

## Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno e instalado las dependencias,
puedes arrancar el proyecto ejecutando:

    flask run
