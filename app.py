from fastapi import FastAPI
from fastapi import HTTPException
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

# Inicializamos el diccionario que se utilizará
# para guardar los datos
predicciones_db = {}


# Ruta para obtener todas las predicciones
@app.get("/predicciones/")
def obtener_predicciones():
    return predicciones_db

# Ruta para obtener todas un predicción específica por ID
@app.get("/prediccion/{id}")
def obtener_prediccion(id:int):
    if id in predicciones_db:
        return predicciones_db[id]
    else:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")

# Ruta para realizar una nueva predicción
@app.post("/predicciones")
def crear_prediccion(cryosleep: int, age: int, vip: int,
                      homeplanet_earth: int, homeplanet_europa: int,
                      homeplanet_mars: int, destination_crancri: int,
                      destination_pso: int, destination_trappist: int):


    with open("src/modelo_entrenado.pkl", "rb") as f:
        model = pickle.load(f)

    new_data = pd.DataFrame(
        {'CryoSleep': [cryosleep], 'Age': [age], 'VIP': [vip], 'HomePlanet_Earth': [homeplanet_earth],
         'HomePlanet_Europa': [homeplanet_europa], 'HomePlanet_Mars': [homeplanet_mars],
         'Destination_55 Cancri e': [destination_crancri], 'Destination_PSO J318.5-22': [destination_pso],
         'Destination_TRAPPIST-1e': [destination_trappist]})

    input_data = np.array(new_data).reshape(1, -1)  # Convertir a un arreglo de NumPy

    # Realizar la predicción con el modelo entrenado
    prediccion = model.predict(input_data)
    prediccion_serializada = prediccion.item()

    # Agregar la predicción al diccionario
    id_contador = len(predicciones_db) + 1
    predicciones_db[id_contador] = {
        "id": id_contador,
        "CryoSleep": cryosleep,
        "Age": age,
        "VIP": vip,
        "HomePlanet_Earth": homeplanet_earth,
        "HomePlanet_Europa": homeplanet_europa,
        "HomePlanet_Mars": homeplanet_mars,
        "Destination_Cancri": destination_crancri,
        "Destination_PSO": destination_pso,
        "Destination_Trappist": destination_trappist,
        "prediction": prediccion_serializada
    }
    return predicciones_db[id_contador]

# Ruta para actualizar los datos por ID
@app.put("/prediccion/{id}")
def actualizar_prediccion(id:int, cryosleep: int, age: int, vip: int,
                      homeplanet_earth: int, homeplanet_europa: int,
                      homeplanet_mars: int, destination_crancri: int,
                      destination_pso: int, destination_trappist: int):
    if id in predicciones_db:

        with open("src/modelo_entrenado.pkl", "rb") as f:
            model = pickle.load(f)

        udpdate_data = pd.DataFrame(
            {'CryoSleep': [cryosleep], 'Age': [age], 'VIP': [vip], 'HomePlanet_Earth': [homeplanet_earth],
             'HomePlanet_Europa': [homeplanet_europa], 'HomePlanet_Mars': [homeplanet_mars],
             'Destination_55 Cancri e': [destination_crancri], 'Destination_PSO J318.5-22': [destination_pso],
             'Destination_TRAPPIST-1e': [destination_trappist]})

        input_data = np.array(udpdate_data).reshape(1, -1)  # Convertir a un arreglo de NumPy

        # Realizar la predicción con el modelo entrenado
        prediccion = model.predict(input_data)
        prediccion_serializada = prediccion.item()

        predicciones_db[id] = {
            "id": id,
            "CryoSleep": cryosleep,
            "Age": age,
            "VIP": vip,
            "HomePlanet_Earth": homeplanet_earth,
            "HomePlanet_Europa": homeplanet_europa,
            "HomePlanet_Mars": homeplanet_mars,
            "Destination_Cancri": destination_crancri,
            "Destination_PSO": destination_pso,
            "Destination_Trappist": destination_trappist,
            "prediction": prediccion_serializada
        }

        return predicciones_db[id]
    else:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")

# Ruta para eliminar una predicción por ID
@app.delete("/prediccion/{id}")
def eliminar_prediccion(id:int):
    if id in predicciones_db:
        del predicciones_db[id]
        return {"message":"Predicción eliminada"}
    else:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
