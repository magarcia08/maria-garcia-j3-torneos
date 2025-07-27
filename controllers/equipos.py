import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA = os.path.join(DB_FILE, "equipos.json")

def crear_equipo():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA)
    nuevo_id = f"EQ{len(equipos) + 1:03}"
    nombre = vd.validatetext("Nombre del equipo: ").title()
    fundacion = input("Fecha de fundación (YYYY-MM-DD): ")
    pais = vd.validatetext("País: ").title()
    liga_id = input("ID de la liga a la que pertenece: ").upper()

    equipo = {
        "id": nuevo_id,
        "nombre": nombre,
        "fundacion": fundacion,
        "pais": pais,
        "liga_id": liga_id
    }
    equipos.append(equipo)
    cf.escribir_json(RUTA, equipos)
    print("✅ Equipo registrado exitosamente")
    sc.pausar()

def listar_equipos():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA)
    print("\n--- LISTADO DE EQUIPOS ---")
    for equipo in equipos:
        print(f"ID: {equipo['id']} | Nombre: {equipo['nombre']} | País: {equipo['pais']} | Fundación: {equipo['fundacion']} | Liga: {equipo['liga_id']}")
    sc.pausar()

def actualizar_equipo():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA)
    id_equipo = input("Ingrese ID del equipo a actualizar: ").upper()
    for i, equipo in enumerate(equipos):
        if equipo["id"] == id_equipo:
            nombre = vd.validatetext("Nuevo nombre: ")
            fundacion = input("Nueva fecha de fundación: ")
            pais = vd.validatetext("Nuevo país: ")
            liga_id = input("Nuevo ID liga: ").upper()
            equipos[i] = {
                "id": id_equipo,
                "nombre": nombre,
                "fundacion": fundacion,
                "pais": pais,
                "liga_id": liga_id
            }
            cf.escribir_json(RUTA, equipos)
            print("✅ Equipo actualizado")
            break
    else:
        print("❌ Equipo no encontrado")
    sc.pausar()

def eliminar_equipo():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA)
    id_equipo = input("Ingrese ID del equipo a eliminar: ").upper()
    for i, equipo in enumerate(equipos):
        if equipo["id"] == id_equipo:
            del equipos[i]
            cf.escribir_json(RUTA, equipos)
            print("✅ Equipo eliminado")
            break
    else:
        print("❌ Equipo no encontrado")
    sc.pausar()

def menu_equipos():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ EQUIPOS ---")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Actualizar equipo")
        print("4. Eliminar equipo")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": crear_equipo()
        elif op == "2": listar_equipos()
        elif op == "3": actualizar_equipo()
        elif op == "4": eliminar_equipo()
        elif op == "0": break
        else: print("Opción inválida")
