import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

# utilice os.path.join para asegurar la compatibilidad entre s.o
RUTA_PARTIDOS = os.path.join(DB_FILE, "partidos.json")
RUTA_EQUIPOS = os.path.join(DB_FILE, "equipos.json")
RUTA_LIGAS = os.path.join(DB_FILE, "ligas.json")
RUTA_TORNEOS = os.path.join(DB_FILE, "torneos.json")

def registrar_partido():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA_PARTIDOS)
    equipos = cf.leer_json(RUTA_EQUIPOS)
    nuevo_id = f"PT{len(partidos) + 1:03}"
    fecha = input("Fecha del partido (YYYY-MM-DD): ")
    id_equipo_local = input("ID del equipo local: ").upper()
    id_equipo_visitante = input("ID del equipo visitante: ").upper()

    if id_equipo_local == id_equipo_visitante:
        print("❌ No pueden enfrentarse el mismo equipo")
        sc.pausar()
        return

    if not any(e["id"] == id_equipo_local for e in equipos):
        print("❌ Equipo local no encontrado")
        sc.pausar()
        return
    if not any(e["id"] == id_equipo_visitante for e in equipos):
        print("❌ Equipo visitante no encontrado")
        sc.pausar()
        return

    # Validar si ambos equipos pertenecen al mismo torneo o liga
    tipo_local = next(e for e in equipos if e["id"] == id_equipo_local)["competencia_tipo"]
    tipo_visita = next(e for e in equipos if e["id"] == id_equipo_visitante)["competencia_tipo"]
    id_comp_local = next(e for e in equipos if e["id"] == id_equipo_local)["competencia_id"]
    id_comp_visita = next(e for e in equipos if e["id"] == id_equipo_visitante)["competencia_id"]

    if tipo_local != tipo_visita or id_comp_local != id_comp_visita:
        print("❌ Los equipos no pertenecen a la misma liga o torneo")
        sc.pausar()
        return

    goles_local = vd.validateInt("Goles del equipo local: ")
    goles_visitante = vd.validateInt("Goles del equipo visitante: ")

    partido = {
        "id": nuevo_id,
        "fecha": fecha,
        "equipo_local": id_equipo_local,
        "equipo_visitante": id_equipo_visitante,
        "goles_local": goles_local,
        "goles_visitante": goles_visitante,
        "competencia_tipo": tipo_local,
        "competencia_id": id_comp_local
    }

    partidos.append(partido)
    cf.escribir_json(RUTA_PARTIDOS, partidos)
    print("✅ Partido registrado exitosamente")
    sc.pausar()

def listar_partidos():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA_PARTIDOS)
    print("\n--- LISTADO DE PARTIDOS ---")
    for p in partidos:
        print(f"ID: {p['id']} | Fecha: {p['fecha']} | {p['equipo_local']} ({p['goles_local']}) vs ({p['goles_visitante']}) {p['equipo_visitante']} | {p['competencia_tipo'].capitalize()} {p['competencia_id']}")
    sc.pausar()

def actualizar_partido():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA_PARTIDOS)
    equipos = cf.leer_json(RUTA_EQUIPOS)
    id_partido = input("Ingrese ID del partido a actualizar: ").upper()
    for i, p in enumerate(partidos):
        if p["id"] == id_partido:
            fecha = input("Nueva fecha (YYYY-MM-DD): ")
            id_equipo_local = input("Nuevo ID equipo local: ").upper()
            id_equipo_visitante = input("Nuevo ID equipo visitante: ").upper()
            if id_equipo_local == id_equipo_visitante:
                print("Mismo equipo no puede jugar contra si mismo ❌")
                sc.pausar()
                return
            if not any(e["id"] == id_equipo_local for e in equipos):
                print("❌ Equipo local no encontrado")
                sc.pausar()
                return
            if not any(e["id"] == id_equipo_visitante for e in equipos):
                print("❌ Equipo visitante no encontrado")
                sc.pausar()
                return
            tipo_local = next(e for e in equipos if e["id"] == id_equipo_local)["competencia_tipo"]
            tipo_visita = next(e for e in equipos if e["id"] == id_equipo_visitante)["competencia_tipo"]
            id_comp_local = next(e for e in equipos if e["id"] == id_equipo_local)["competencia_id"]
            id_comp_visita = next(e for e in equipos if e["id"] == id_equipo_visitante)["competencia_id"]

            if tipo_local != tipo_visita or id_comp_local != id_comp_visita:
                print("Los equipos no pertenecen a la misma competencia")
                sc.pausar()
                return

            goles_local = vd.validateInt("Nuevo goles local: ")
            goles_visitante = vd.validateInt("Nuevo goles visitante: ")

            partidos[i] = {
                "id": id_partido,
                "fecha": fecha,
                "equipo_local": id_equipo_local,
                "equipo_visitante": id_equipo_visitante,
                "goles_local": goles_local,
                "goles_visitante": goles_visitante,
                "competencia_tipo": tipo_local,
                "competencia_id": id_comp_local
            }
            cf.escribir_json(RUTA_PARTIDOS, partidos)
            print("Partido actualizado ")
            break
    else:
        print("❌ Partido no encontrado")
    sc.pausar()

def eliminar_partido():
    sc.limpiar_pantalla()
    partidos = cf.leer_json(RUTA_PARTIDOS)
    id_partido = input("Ingrese ID del partido a eliminar: ").upper()
    for i, p in enumerate(partidos):
        if p["id"] == id_partido:
            del partidos[i]
            cf.escribir_json(RUTA_PARTIDOS, partidos)
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
        if op == "1": registrar_partido()
        elif op == "2": listar_partidos()
        elif op == "3": actualizar_partido()
        elif op == "4": eliminar_partido()
        elif op == "0": break
        else: print("Opción inválida")