import utils.corefiles as cf
import utils.screenControllers as sc
import os
from config import DB_FILE
from datetime import datetime

RUTA_JUGADORES = os.path.join(DB_FILE, "jugadores.json")
RUTA_PARTIDOS = os.path.join(DB_FILE, "partidos.json")

# Edad actual desde fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

def jugador_mas_joven():
    jugadores = cf.leer_json(RUTA_JUGADORES)
    if not jugadores:
        print("❌ No hay jugadores registrados")
        return
    mas_joven = min(jugadores, key=lambda j: calcular_edad(j["fecha_nacimiento"]))
    edad = calcular_edad(mas_joven["fecha_nacimiento"])
    print(f"🎉 Jugador más joven: {mas_joven['nombre']} ({edad} años)")

def jugador_mas_veterano():
    jugadores = cf.leer_json(RUTA_JUGADORES)
    if not jugadores:
        print("❌ No hay jugadores registrados")
        return
    veterano = max(jugadores, key=lambda j: calcular_edad(j["fecha_nacimiento"]))
    edad = calcular_edad(veterano["fecha_nacimiento"])
    print(f"Jugador más veterano: {veterano['nombre']} ({edad} años)")

def total_goles():
    partidos = cf.leer_json(RUTA_PARTIDOS)
    if not partidos:
        print("❌ No hay partidos registrados")
        return
    goles = sum(p["goles_local"] + p["goles_visitante"] for p in partidos)
    print(f"Goles totales anotados: {goles}")

def menu_estadisticas():
    while True:
        sc.limpiar_pantalla()
        print("\n📊 MENÚ ESTADÍSTICAS")
        print("1. Jugador más joven")
        print("2. Jugador mas veterano")
        print("3. Total de goles")
        print("0. Volver")
        op = input("Opcion: ")
        if op == "1": jugador_mas_joven(); sc.pausar()
        elif op == "2": jugador_mas_veterano(); sc.pausar()
        elif op == "3": total_goles(); sc.pausar()
        elif op == "0": break
        else: print("❌ Opción inválida")