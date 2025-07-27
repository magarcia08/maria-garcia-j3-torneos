import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

RUTA_JUGADORES = os.path.join(DB_FILE, "jugadores.json")
RUTA_TRANSFERENCIAS = os.path.join(DB_FILE, "transferencias.json")

def solicitar_transferencia():
    sc.limpiar_pantalla()
    jugadores = cf.leer_json(RUTA_JUGADORES)
    transferencias = cf.leer_json(RUTA_TRANSFERENCIAS)

    id_jugador = input("ID del jugador a transferir: ").upper()
    jugador = next((j for j in jugadores if j['id'] == id_jugador), None)

    if not jugador:
        print("❌ Jugador no encontrado")
        sc.pausar()
        return

    print(f"Jugador: {jugador['nombre']} | Equipo actual: {jugador['equipo_id']}")
    equipo_destino = input("ID del equipo destino: ").upper()
    tipo = input("Tipo de transferencia (venta/préstamo): ").lower()
    valor = vd.validateInt("Valor ofrecido: ")
    fecha = input("Fecha de transferencia (YYYY-MM-DD): ")

    confirmar = input(f"¿Aceptar la transferencia al equipo {equipo_destino} por ${valor}? (s/n): ").lower()
    if confirmar == "s":
        jugador['equipo_id'] = equipo_destino
        for i, j in enumerate(jugadores):
            if j['id'] == jugador['id']:
                jugadores[i] = jugador
                break

        nueva_transferencia = {
            "id": f"TF{len(transferencias) + 1:03}",
            "jugador_id": jugador['id'],
            "nombre_jugador": jugador['nombre'],
            "equipo_origen": jugador['equipo_id'],
            "equipo_destino": equipo_destino,
            "tipo": tipo,
            "valor": valor,
            "fecha": fecha
        }
        transferencias.append(nueva_transferencia)
        cf.escribir_json(RUTA_JUGADORES, jugadores)
        cf.escribir_json(RUTA_TRANSFERENCIAS, transferencias)
        print("✅ Transferencia completada")
    else:
        print("❌ Transferencia cancelada")
    sc.pausar()

def listar_transferencias():
    sc.limpiar_pantalla()
    transferencias = cf.leer_json(RUTA_TRANSFERENCIAS)
    print("\n--- HISTORIAL DE TRANSFERENCIAS ---")
    for t in transferencias:
        print(f"ID: {t['id']} | Jugador: {t['nombre_jugador']} | Origen: {t['equipo_origen']} -> Destino: {t['equipo_destino']} | Tipo: {t['tipo']} | Valor: ${t['valor']} | Fecha: {t['fecha']}")
    sc.pausar()

def menu_transferencias():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ TRANSFERENCIAS ---")
        print("1. Solicitar transferencia")
        print("2. Ver historial")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": solicitar_transferencia()
        elif op == "2": listar_transferencias()
        elif op == "0": break
        else: print("Opción inválida")
