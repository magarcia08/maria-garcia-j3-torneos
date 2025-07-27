import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA = os.path.join(DB_FILE, "partidos.json")

def crear_partido():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA)
    nuevo_id = f"PA{len(partidos) + 1:03}"
    equipo_local = input("ID del equipo local: ").upper()
    equipo_visitante = input("ID del equipo visitante: ").upper()
    goles_local = vd.validateInt("Goles equipo local: ")
    goles_visitante = vd.validateInt("Goles equipo visitante: ")
    fecha = input("Fecha del partido (YYYY-MM-DD): ")
    torneo_id = input("ID del torneo: ").upper()

    partido = {
        "id": nuevo_id,
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "goles_local": goles_local,
        "goles_visitante": goles_visitante,
        "fecha": fecha,
        "torneo_id": torneo_id
    }
    partidos.append(partido)
    cf.escribir_json(RUTA, partidos)
    print("✅ Partido registrado exitosamente")
    sc.pausar()

def listar_partidos():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA)
    print("\n--- LISTADO DE PARTIDOS ---")
    for p in partidos:
        print(f"ID: {p['id']} | {p['equipo_local']} ({p['goles_local']}) vs ({p['goles_visitante']}) {p['equipo_visitante']} | Fecha: {p['fecha']} | Torneo: {p['torneo_id']}")
    sc.pausar()

def actualizar_partido():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA)
    id_partido = input("Ingrese ID del partido a actualizar: ").upper()
    for i, p in enumerate(partidos):
        if p["id"] == id_partido:
            equipo_local = input("Nuevo equipo local: ").upper()
            equipo_visitante = input("Nuevo equipo visitante: ").upper()
            goles_local = vd.validateInt("Nuevos goles equipo local: ")
            goles_visitante = vd.validateInt("Nuevos goles equipo visitante: ")
            fecha = input("Nueva fecha del partido: ")
            torneo_id = input("Nuevo ID del torneo: ").upper()
            partidos[i] = {
                "id": id_partido,
                "equipo_local": equipo_local,
                "equipo_visitante": equipo_visitante,
                "goles_local": goles_local,
                "goles_visitante": goles_visitante,
                "fecha": fecha,
                "torneo_id": torneo_id
            }
            cf.escribir_json(RUTA, partidos)
            print("✅ Partido actualizado")
            break
    else:
        print("❌ Partido no encontrado")
    sc.pausar()

def eliminar_partido():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA)
    id_partido = input("Ingrese ID del partido a eliminar: ").upper()
    for i, p in enumerate(partidos):
        if p["id"] == id_partido:
            del partidos[i]
            cf.escribir_json(RUTA, partidos)
            print("✅ Partido eliminado")
            break
    else:
        print("❌ Partido no encontrado")
    sc.pausar()

def menu_partidos():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ PARTIDOS ---")
        print("1. Registrar partido")
        print("2. Listar partidos")
        print("3. Actualizar partido")
        print("4. Eliminar partido")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": crear_partido()
        elif op == "2": listar_partidos()
        elif op == "3": actualizar_partido()
        elif op == "4": eliminar_partido()
        elif op == "0": break
        else: print("Opción inválida")
