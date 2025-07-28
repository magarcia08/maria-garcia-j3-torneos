import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA = os.path.join(DB_FILE, "ligas.json")

def crear_liga():
    sc.limpiar_pantalla()
    ligas = cf.leer_json(RUTA)
    # LIG{n:03} para generar id como LIG001, LIG002, etc.
    nuevo_id = f"LIG{len(ligas) + 1:03}"
    nombre = vd.validatetext("Nombre de la liga: ").title()
    pais = vd.validatetext("País de la liga: ").title()
    fechainicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fechafin = input("Fecha de finalización (YYYY-MM-DD): ")

    liga = {
        "id": nuevo_id,
        "nombre": nombre,
        "pais": pais,
        "fechainicio": fechainicio,
        "fechafin": fechafin
    }
    ligas.append(liga)
    cf.escribir_json(RUTA, ligas)
    print("✅ Liga registrada exitosamente")
    sc.pausar()

def listar_ligas():
    sc.limpiar_pantalla()
    ligas = cf.leer_json(RUTA)
    print("\n--- LISTADO DE LIGAS ---")
    for liga in ligas:
        print(f"ID: {liga['id']} | Nombre: {liga['nombre']} | País: {liga['pais']} | Inicio: {liga['fechainicio']} | Fin: {liga['fechafin']}")
    sc.pausar()

def actualizar_liga():
    sc.limpiar_pantalla()
    ligas = cf.leer_json(RUTA)
    id_liga = input("Ingrese ID de la liga a actualizar: ").upper()
    for i, liga in enumerate(ligas):
        if liga["id"] == id_liga:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            pais = vd.validatetext("Nuevo país: ").title()
            fechainicio = input("Nueva fecha de inicio: ")
            fechafin = input("Nueva fecha de finalización: ")
            ligas[i] = {
                "id": id_liga,
                "nombre": nombre,
                "pais": pais,
                "fechainicio": fechainicio,
                "fechafin": fechafin
            }
            cf.escribir_json(RUTA, ligas)
            print("✅ Liga actualizada")
            break
    else:
        print("❌ Liga no encontrada")
    sc.pausar()

def eliminar_liga():
    sc.limpiar_pantalla()
    ligas = cf.leer_json(RUTA)
    id_liga = input("Ingrese ID de la liga a eliminar: ").upper()
    for i, liga in enumerate(ligas):
        if liga["id"] == id_liga:
            del ligas[i]
            cf.escribir_json(RUTA, ligas)
            print("✅ Liga eliminada")
            break
    else:
        print("❌ Liga no encontrada")
    sc.pausar()

def menu_ligas():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ LIGAS ---")
        print("1. Registrar liga")
        print("2. Listar ligas")
        print("3. Actualizar liga")
        print("4. Eliminar liga")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": crear_liga()
        elif op == "2": listar_ligas()
        elif op == "3": actualizar_liga()
        elif op == "4": eliminar_liga()
        elif op == "0": break
        else: print("Opción inválida")