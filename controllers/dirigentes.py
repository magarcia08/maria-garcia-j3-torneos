import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

# Ruta del archivo JSON para los dirigentes
# utilice os.path.join para asegurar la compatibilidad entre s.o
RUTA = os.path.join(DB_FILE, "dirigentes.json")

# crud
def crear_dirigente():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA)
    # DI{n:03} para generar id como DI001, DI002, etc.
    nuevo_id = f"DI{len(dirigentes) + 1:03}"
    nombre = vd.validatetext("Nombre del dirigente: ").title()
    cargo = vd.validatetext("Cargo: ").title()
    equipo_id = input("ID del equipo al que pertenece: ").upper()

    dirigente = {
        "id": nuevo_id,
        "nombre": nombre,
        "cargo": cargo,
        "equipo_id": equipo_id
    }
    dirigentes.append(dirigente)
    cf.escribir_json(RUTA, dirigentes)
    print("✅ Dirigente registrado exitosamente")
    sc.pausar()

def listar_dirigentes():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA)
    print("\n--- LISTADO DE DIRIGENTES ---")
    for d in dirigentes:
        print(f"ID: {d['id']} | Nombre: {d['nombre']} | Cargo: {d['cargo']} | Equipo: {d['equipo_id']}")
    sc.pausar()

def actualizar_dirigente():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA)
    id_dirigente = input("Ingrese ID del dirigente a actualizar: ").upper()
    for i, d in enumerate(dirigentes):
        if d["id"] == id_dirigente:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            cargo = vd.validatetext("Nuevo cargo: ").title()
            equipo_id = input("Nuevo ID de equipo: ").upper()
            dirigentes[i] = {
                "id": id_dirigente,
                "nombre": nombre,
                "cargo": cargo,
                "equipo_id": equipo_id
            }
            cf.escribir_json(RUTA, dirigentes)
            print("✅ Dirigente actualizado")
            break
    else:
        print("❌ Dirigente no encontrado")
    sc.pausar()

def eliminar_dirigente():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA)
    id_dirigente = input("Ingrese ID del dirigente a eliminar: ").upper()
    for i, d in enumerate(dirigentes):
        if d["id"] == id_dirigente:
            del dirigentes[i]
            cf.escribir_json(RUTA, dirigentes)
            print("✅ Dirigente eliminado")
            break
    else:
        print("❌ Dirigente no encontrado")
    sc.pausar()

def menu_dirigentes():
    while True:
        sc.limpiar_pantalla()
        print("\n--- MENÚ DIRIGENTES ---")
        print("1. Registrar dirigente")
        print("2. Listar dirigentes")
        print("3. Actualizar dirigente")
        print("4. Eliminar dirigente")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": crear_dirigente()
        elif op == "2": listar_dirigentes()
        elif op == "3": actualizar_dirigente()
        elif op == "4": eliminar_dirigente()
        elif op == "0": break
        else: print("Opción inválida")
