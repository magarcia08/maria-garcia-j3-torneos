import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

# utilice os.path.join para asegurar la compatibilidad entre s.o

RUTA_JUGADORES = os.path.join(DB_FILE, "jugadores.json")
RUTA_EQUIPOS = os.path.join(DB_FILE, "equipos.json")

def crear_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    equipos = cf.leer_json(RUTA_EQUIPOS)
    # PJ{n:03} para generar id como PJ001, PJ002, etc
    nuevo_id = f"PJ{len(jugadores) + 1:03}"
    nombre = vd.validatetext("Nombre del jugador: ").title()
    posicion = vd.validatetext("Posición (Ej: Defensa, Delantero, Portero): ").title()
    dorsal = vd.validateInt("Número dorsal: ")
    id_equipo = input("ID del equipo al que pertenece: ").upper()

    if not any(e["id"] == id_equipo for e in equipos):
        print("❌ El equipo no existe. Regístrelo primero.")
        sc.pausar()
        return

    jugador = {
        "id": nuevo_id,
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "id_equipo": id_equipo
    }

    jugadores.append(jugador)
    cf.escribir_json(RUTA_JUGADORES, jugadores)
    print("✅ Jugador registrado exitosamente")
    sc.pausar()

def listar_jugadores():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    print("\n--- LISTADO DE JUGADORES ---")
    for j in jugadores:
        print(f"ID: {j['id']} | Nombre: {j['nombre']} | Posición: {j['posicion']} | Dorsal: {j['dorsal']} | Equipo: {j['id_equipo']}")
    sc.pausar()

def actualizar_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    equipos = cf.leer_json(RUTA_EQUIPOS)
    id_jugador = input("Ingrese ID del jugador a actualizar: ").upper()
    for i, j in enumerate(jugadores):
        if j["id"] == id_jugador:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            posicion = vd.validatetext("Nueva posición: ").title()
            dorsal = vd.validateInt("Nuevo dorsal: ")
            id_equipo = input("Nuevo ID del equipo: ").upper()
            if not any(e["id"] == id_equipo for e in equipos):
                print("❌ El equipo no existe.")
                sc.pausar()
                return
            jugadores[i] = {
                "id": id_jugador,
                "nombre": nombre,
                "posicion": posicion,
                "dorsal": dorsal,
                "id_equipo": id_equipo
            }
            cf.escribir_json(RUTA_JUGADORES, jugadores)
            print("✅ Jugador actualizado")
            break
    else:
        print("❌ Jugador no encontrado")
    sc.pausar()

def eliminar_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    id_jugador = input("Ingrese ID del jugador a eliminar: ").upper()
    for i, j in enumerate(jugadores):
        if j["id"] == id_jugador:
            del jugadores[i]
            cf.escribir_json(RUTA_JUGADORES, jugadores)
            print("✅ Jugador eliminado")
            break
    else:
        print("❌ Jugador no encontrado")
    sc.pausar()

def menu_jugadores():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ JUGADORES ---")
        print("1. Registrar jugador")
        print("2. Listar jugadores")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": crear_jugador()
        elif op == "2": listar_jugadores()
        elif op == "3": actualizar_jugador()
        elif op == "4": eliminar_jugador()
        elif op == "0": break
        else: print("Opción inválida")
