import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA = os.path.join(DB_FILE, "jugadores.json")

def crear_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA)
    nuevo_id = f"JU{len(jugadores) + 1:03}"
    nombre = vd.validatetext("Nombre del jugador: ").title()
    posicion = vd.validatetext("Posición: ").title()
    dorsal = vd.validateInt("Número dorsal: ")
    equipo_id = input("ID del equipo: ").upper()
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")

    jugador = {
        "id": nuevo_id,
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "equipo_id": equipo_id,
        "fecha_nacimiento": fecha_nacimiento
    }
    jugadores.append(jugador)
    cf.escribir_json(RUTA, jugadores)
    print("✅ Jugador registrado exitosamente")
    sc.pausar()

def listar_jugadores():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA)
    print("\n--- LISTADO DE JUGADORES ---")
    for jugador in jugadores:
        print(f"ID: {jugador['id']} | Nombre: {jugador['nombre']} | Posición: {jugador['posicion']} | Dorsal: {jugador['dorsal']} | Equipo: {jugador['equipo_id']} | Nacimiento: {jugador['fecha_nacimiento']}")
    sc.pausar()

def actualizar_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA)
    id_jugador = input("Ingrese ID del jugador a actualizar: ").upper()
    for i, jugador in enumerate(jugadores):
        if jugador["id"] == id_jugador:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            posicion = vd.validatetext("Nueva posición: ").title()
            dorsal = vd.validateInt("Nuevo dorsal: ")
            equipo_id = input("Nuevo ID de equipo: ").upper()
            fecha_nacimiento = input("Nueva fecha de nacimiento: ")
            jugadores[i] = {
                "id": id_jugador,
                "nombre": nombre,
                "posicion": posicion,
                "dorsal": dorsal,
                "equipo_id": equipo_id,
                "fecha_nacimiento": fecha_nacimiento
            }
            cf.escribir_json(RUTA, jugadores)
            print("✅ Jugador actualizado")
            break
    else:
        print("❌ Jugador no encontrado")
    sc.pausar()

def eliminar_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA)
    id_jugador = input("Ingrese ID del jugador a eliminar: ").upper()
    for i, jugador in enumerate(jugadores):
        if jugador["id"] == id_jugador:
            del jugadores[i]
            cf.escribir_json(RUTA, jugadores)
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
