¡Hola! Me alegra ayudarte a crear un README.md para tu proyecto. Aquí te dejo una propuesta:

**Spaceship Titanic API**
==========================

**Resumen**
-----------

Este proyecto crea una API que consume el modelo entrenado desarrollado en el proyecto [Spaceship Titanic Kaggle](https://github.com/walterrivarola/SpaceshipTitanicKaggle). La API utiliza FastAPI y permite realizar predicciones sobre nuevos datos para determinar si un pasajero puede ser teletransportado a otra dimensión o no.

**Tecnologías utilizadas**
-------------------------

* Python 3.11
* FastAPI
* Pandas
* NumPy
* Pickle
* Docker

**Funcionalidades**
-------------------

La API ofrece las siguientes funcionalidades:

* **GET**: Obtener información sobre el modelo entrenado y la API.
* **POST**: Realizar predicciones sobre nuevos datos.
* **PUT**: Actualizar el modelo entrenado con nuevos datos.
* **DELETE**: Eliminar el modelo entrenado.

**Despliegue con Docker**
-------------------------

Para desplegar la API utilizando Docker, sigue los siguientes pasos:

1. Construye la imagen de Docker ejecutando el comando `docker build -t spaceship-titanic-api.` en la raíz del proyecto.
2. Inicia el contenedor ejecutando el comando `docker run -p 8000:8000 spaceship-titanic-api`.

**Uso**
-----

Una vez desplegada la API, puedes interactuar con ella utilizando herramientas como `curl` o un cliente HTTP de tu preferencia. Por ejemplo, para realizar una predicción, puedes enviar una solicitud `POST` a `http://localhost:8000/predict` con los datos del pasajero en el cuerpo de la solicitud.

**Modelo entrenado**
-------------------

El modelo entrenado se encuentra en el archivo `src/modelo_entrenado.pkl`. Este archivo fue generado en el proyecto [Spaceship Titanic Kaggle](https://github.com/walterrivarola/SpaceshipTitanicKaggle) y se utiliza en esta API para realizar predicciones.
