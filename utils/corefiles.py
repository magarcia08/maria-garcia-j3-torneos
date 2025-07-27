import json
import os

#lee json
def leer_json(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

#guardar JSON
def escribir_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

#actualizar json
def update_json(diccionario, lista):
    for archivo in lista:
        ruta = f"data/{archivo.lower()}.json"
        datos = leer_json(ruta)
        for k, v in diccionario.items():
            datos.append({"id": k, **v})
        escribir_json(ruta, datos)
        return False
    return True