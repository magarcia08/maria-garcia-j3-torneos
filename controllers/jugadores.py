import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA_JUGADORES = os.path.join(DB_FILE, "jugadores.json")
RUTA_EQUIPOS = os.path.join(DB_FILE, "equipos.json")

def crear_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    equipos = cf.leer_json(RUTA_EQUIPOS)

    nombre = vd.validatetext("Nombre del jugador: ")
    posicion = vd.validatetext("Posición: ")
    dorsal = vd.validateInt("Número dorsal: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")

    print("\nEquipos disponibles:")
    for e in equipos:
        print(f"{e['id']} - {e['nombre']}")
    id_equipo = input("ID del equipo al que pertenece: ").upper()
    if not any(e['id'] == id_equipo for e in equipos):
        print("❌ El equipo no existe")
        sc.pausar()
        return

    nuevo = {
        "id": f"JUG{len(jugadores)+1:03}",
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "fecha_nacimiento": fecha_nacimiento,
        "id_equipo": id_equipo
    }

    jugadores.append(nuevo)
    cf.escribir_json(RUTA_JUGADORES, jugadores)
    print("✅ Jugador registrado con éxito")
    sc.pausar()

def listar_jugadores():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    print("\n--- LISTA DE JUGADORES ---")
    for j in jugadores:
        print(f"{j['id']} | {j['nombre']} | Posición: {j['posicion']} | Dorsal: {j['dorsal']} | Nacimiento: {j['fecha_nacimiento']} | Equipo: {j['id_equipo']}")
    sc.pausar()

def actualizar_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    listar_jugadores()
    id_buscar = input("ID del jugador a modificar: ").upper()

    for j in jugadores:
        if j['id'] == id_buscar:
            print("Actualiza los datos (deja en blanco si no deseas cambiar):")
            nombre = input("Nuevo nombre: ") or j['nombre']
            posicion = input("Nueva posición: ") or j['posicion']
            dorsal = input("Nuevo dorsal: ") or str(j['dorsal'])
            fecha_nacimiento = input("Nueva fecha de nacimiento (YYYY-MM-DD): ") or j['fecha_nacimiento']
            id_equipo = input("Nuevo ID de equipo: ") or j['id_equipo']

            j.update({
                "nombre": nombre,
                "posicion": posicion,
                "dorsal": int(dorsal),
                "fecha_nacimiento": fecha_nacimiento,
                "id_equipo": id_equipo
            })
            cf.escribir_json(RUTA_JUGADORES, jugadores)
            print("✅ Jugador actualizado")
            break
    else:
        print("❌ Jugador no encontrado")

    sc.pausar()

def eliminar_jugador():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    listar_jugadores()
    id_eliminar = input("ID del jugador a eliminar: ").upper()
    jugadores = [j for j in jugadores if j['id'] != id_eliminar]
    cf.escribir_json(RUTA_JUGADORES, jugadores)
    print("✅ Jugador eliminado")
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
