"""
Autor: Maria Alejandra Garcia Merchan
Fecha: 2025-07-27
Descripción: Este es el punto de entrada principal para el gestor de torneos de fútbol.
Este proyecto permite gestionar equipos, jugadores, dirigentes, partidos, ligas, torneos, 
transferencias y estadísticas de fútbol.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# se creo la linea anterior para que pueda importar los modulos de controllers y utils, y utilizar el run code
# segunda forma de inicializar el proyecto es python "3" -m app.main

from controllers.equipos import menu_equipos
from controllers.jugadores import menu_jugadores
from controllers.dirigentes import menu_dirigentes
from controllers.partidos import menu_partidos
from controllers.ligas import menu_ligas
from controllers.torneos import menu_torneos
from controllers.transferencias import menu_transferencias
from controllers.estadisticas import menu_estadisticas
import utils.screenControllers as sc


# Punto de entrada principal del gestor de torneos de fútbol
def menu_principal():
    while True:
        sc.limpiar_pantalla()
        print("\n===== GESTOR DE TORNEO DE FÚTBOL ===")
        print("1. Equipos")
        print("2. Jugadores")
        print("3. Dirigentes")
        print("4. Partidos")
        print("5. Ligas")
        print("6. Torneos")
        print("7. Transferencias")
        print("8. Estadísticas")
        print("0. Salir")
        op = input("Seleccione una opción: ")
        if op == "1": menu_equipos()
        elif op == "2": menu_jugadores()
        elif op == "3": menu_dirigentes()
        elif op == "4": menu_partidos()
        elif op == "5": menu_ligas()
        elif op == "6": menu_torneos()
        elif op == "7": menu_transferencias()
        elif op == "8": menu_estadisticas()
        elif op == "0":
            print("Gracias por usar el sistema. ")
            break
        else:
            print("Opción inválida")
            sc.pausar()

if __name__ == "__main__":
    menu_principal()
