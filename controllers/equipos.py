import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA_EQUIPOS = os.path.join(DB_FILE, "equipos.json")
RUTA_LIGAS = os.path.join(DB_FILE, "ligas.json")
RUTA_TORNEOS = os.path.join(DB_FILE, "torneos.json")

def crear_equipo():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA_EQUIPOS)
    # EQ{n:03} para generar id como EQ001, EQ002, etc
    nuevo_id = f"EQ{len(equipos) + 1:03}"
    nombre = vd.validatetext("Nombre del equipo: ").title()
    pais = vd.validatetext("País del equipo: ").title()
    fecha_fundacion = input("Fecha de fundación (YYYY-MM-DD): ")

    tipo_competencia = input("¿A qué pertenece este equipo? (liga/torneo): ").lower()
    competencia_id = ""

    if tipo_competencia == "liga":
        competencia_id = input("Ingrese ID de la liga: ").upper()
        ligas = cf.leer_json(RUTA_LIGAS)
        if not any(l["id"] == competencia_id for l in ligas):
            print("❌ Liga no encontrada. Regístrela primero.")
            sc.pausar()
            return
    elif tipo_competencia == "torneo":
        competencia_id = input("Ingrese ID del torneo: ").upper()
        torneos = cf.leer_json(RUTA_TORNEOS)
        if not any(t["id"] == competencia_id for t in torneos):
            print("❌ Torneo no encontrado. Regístrelo primero.")
            sc.pausar()
            return
    else:
        print("❌ Tipo de competencia inválido")
        sc.pausar()
        return

    equipo = {
        "id": nuevo_id,
        "nombre": nombre,
        "pais": pais,
        "fecha_fundacion": fecha_fundacion,
        "competencia_tipo": tipo_competencia,
        "competencia_id": competencia_id
    }

    equipos.append(equipo)
    cf.escribir_json(RUTA_EQUIPOS, equipos)
    print("✅ Equipo registrado exitosamente")
    sc.pausar()

def listar_equipos():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA_EQUIPOS)
    print("\n--- LISTADO DE EQUIPOS ---")
    for eq in equipos:
        print(f"ID: {eq['id']} | Nombre: {eq['nombre']} | País: {eq['pais']} | Fundación: {eq['fecha_fundacion']} | Pertenece a: {eq['competencia_tipo'].capitalize()} ({eq['competencia_id']})")
    sc.pausar()

def actualizar_equipo():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA_EQUIPOS)
    id_equipo = input("Ingrese ID del equipo a actualizar: ").upper()
    for i, eq in enumerate(equipos):
        if eq["id"] == id_equipo:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            pais = vd.validatetext("Nuevo país: ").title()
            fecha_fundacion = input("Nueva fecha de fundación: ")
            tipo_competencia = input("Tipo de competencia (liga/torneo): ").lower()
            competencia_id = ""

            if tipo_competencia == "liga":
                competencia_id = input("ID de la liga: ").upper()
                ligas = cf.leer_json(RUTA_LIGAS)
                if not any(l["id"] == competencia_id for l in ligas):
                    print("❌ Liga no encontrada")
                    sc.pausar()
                    return
            elif tipo_competencia == "torneo":
                competencia_id = input("ID del torneo: ").upper()
                torneos = cf.leer_json(RUTA_TORNEOS)
                if not any(t["id"] == competencia_id for t in torneos):
                    print("❌ Torneo no encontrado")
                    sc.pausar()
                    return
            else:
                print("❌ Tipo de competencia inválido")
                sc.pausar()
                return

            equipos[i] = {
                "id": id_equipo,
                "nombre": nombre,
                "pais": pais,
                "fecha_fundacion": fecha_fundacion,
                "competencia_tipo": tipo_competencia,
                "competencia_id": competencia_id
            }
            cf.escribir_json(RUTA_EQUIPOS, equipos)
            print("✅ Equipo actualizado")
            break
    else:
        print("❌ Equipo no encontrado")
    sc.pausar()

def eliminar_equipo():
    sc.limpiar_pantalla()
    equipos = cf.leer_json(RUTA_EQUIPOS)
    id_equipo = input("Ingrese ID del equipo a eliminar: ").upper()
    for i, eq in enumerate(equipos):
        if eq["id"] == id_equipo:
            del equipos[i]
            cf.escribir_json(RUTA_EQUIPOS, equipos)
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
