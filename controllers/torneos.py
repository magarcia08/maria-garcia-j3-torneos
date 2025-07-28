import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA = os.path.join(DB_FILE, "torneos.json")

def crear_torneo():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA)
    # TR{n:03} para generar id como TR001, TR002, etc.
    nuevo_id = f"TR{len(torneos) + 1:03}"
    fechaini = input("Fecha de inicio (YYYY-MM-DD): ")
    fechafin = input("Fecha de fin (YYYY-MM-DD): ")
    pais = vd.validatetext("País: ").title()

    torneo = {
        "id": nuevo_id,
        "fechainicio": fechaini,
        "fechafin": fechafin,
        "pais": pais
    }
    torneos.append(torneo)
    cf.escribir_json(RUTA, torneos)
    print("✅ Torneo registrado exitosamente")
    sc.pausar()

def listar_torneos():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA)
    print("\n--- LISTADO DE TORNEOS ---")
    for torneo in torneos:
        print(f"ID: {torneo['id']} | País: {torneo['pais']} | Inicio: {torneo['fechainicio']} | Fin: {torneo['fechafin']}")
    sc.pausar()

def actualizar_torneo():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA)
    id_torneo = input("Ingrese ID del torneo a actualizar: ").upper()
    for i, torneo in enumerate(torneos):
        if torneo["id"] == id_torneo:
            fechaini = input("Nueva fecha de inicio: ")
            fechafin = input("Nueva fecha de fin: ")
            pais = vd.validatetext("Nuevo país: ").title()
            torneos[i] = {
                "id": id_torneo,
                "fechainicio": fechaini,
                "fechafin": fechafin,
                "pais": pais
            }
            cf.escribir_json(RUTA, torneos)
            print("✅ Torneo actualizado")
            break
    else:
        print("❌ Torneo no encontrado")
    sc.pausar()

def eliminar_torneo():
    sc.limpiar_pantalla()
    torneos = cf.leer_json(RUTA)
    id_torneo = input("Ingrese ID del torneo a eliminar: ").upper()
    for i, torneo in enumerate(torneos):
        if torneo["id"] == id_torneo:
            del torneos[i]
            cf.escribir_json(RUTA, torneos)
            print("✅ Torneo eliminado")
            break
    else:
        print("❌ Torneo no encontrado")
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
        if op == "1": crear_torneo()
        elif op == "2": listar_torneos()
        elif op == "3": actualizar_torneo()
        elif op == "4": eliminar_torneo()
        elif op == "0": break
        else: print("Opción inválida")
