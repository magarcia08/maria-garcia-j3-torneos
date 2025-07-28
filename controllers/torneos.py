import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA_TORNEOS = os.path.join(DB_FILE, "torneos.json")

def registrar_torneo():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA_TORNEOS)
    nuevo_id = f"TR{len(torneos) + 1:03}"
    nombre = vd.validatetext("Nombre del torneo: ").title()
    pais = vd.validatetext("País: ").title()
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de finalización (YYYY-MM-DD): ")

    torneo = {
        "id": nuevo_id,
        "nombre": nombre,
        "pais": pais,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin
    }

    torneos.append(torneo)
    cf.escribir_json(RUTA_TORNEOS, torneos)
    print("✅ Torneo registrado correctamente")
    sc.pausar()

def listar_torneos():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA_TORNEOS)
    print("\n--- LISTADO DE TORNEOS ---")
    for t in torneos:
        print(f"ID: {t['id']} | Nombre: {t['nombre']} | País: {t['pais']} | {t['fecha_inicio']} ➡ {t['fecha_fin']}")
    sc.pausar()

def actualizar_torneo():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA_TORNEOS)
    id_torneo = input("ID del torneo a actualizar: ").upper()
    for i, t in enumerate(torneos):
        if t["id"] == id_torneo:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            pais = vd.validatetext("Nuevo país: ").title()
            fecha_inicio = input("Nueva fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Nueva fecha fin (YYYY-MM-DD): ")

            torneos[i] = {
                "id": id_torneo,
                "nombre": nombre,
                "pais": pais,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin
            }
            cf.escribir_json(RUTA_TORNEOS, torneos)
            print("Torneo actualizado. ")
            break
    else:
        print("❌ Torneo no encontrado")
    sc.pausar()

def eliminar_torneo():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA_TORNEOS)
    id_torneo = input("ID del torneo a eliminar: ").upper()
    for i, t in enumerate(torneos):
        if t["id"] == id_torneo:
            del torneos[i]
            cf.escribir_json(RUTA_TORNEOS, torneos)
            print("✅ Torneo eliminado")
            break
    else:
        print("Torneo no encontrado")
    sc.pausar()

def menu_torneos():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ TORNEOS ---")
        print("1. Registrar torneo")
        print("2. Listar torneos")
        print("3. Actualizar torneo")
        print("4. Eliminar torneo")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": registrar_torneo()
        elif op == "2": listar_torneos()
        elif op == "3": actualizar_torneo()
        elif op == "4": eliminar_torneo()
        elif op == "0": break
        else: print("Opción inválida")
