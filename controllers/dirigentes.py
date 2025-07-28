import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
from config import DB_FILE
import os

# utilice os.path.join para asegurar la compatibilidad entre s.o
RUTA_DIRIGENTES = os.path.join(DB_FILE, "dirigentes.json")
RUTA_LIGAS = os.path.join(DB_FILE, "ligas.json")
RUTA_TORNEOS = os.path.join(DB_FILE, "torneos.json")

#CRUD: Dirigentes
def registrar_dirigente():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA_DIRIGENTES)
    nuevo_id = f"DG{len(dirigentes) + 1:03}"
    nombre = vd.validatetext("Nombre del dirigente: ").title()
    cargo = vd.validatetext("Cargo: ").title()

    tipo_competencia = input("¿Asociado a (liga/torneo)?: ").lower()
    if tipo_competencia not in ["liga", "torneo"]:
        print("❌ Tipo inválido")
        sc.pausar()
        return

    competencia_id = input(f"Ingrese ID de la {tipo_competencia}: ").upper()
    datos = cf.leer_json(RUTA_LIGAS if tipo_competencia == "liga" else RUTA_TORNEOS)

    if not any(x["id"] == competencia_id for x in datos):
        print("❌ ID de competencia no encontrado")
        sc.pausar()
        return

    dirigente = {
        "id": nuevo_id,
        "nombre": nombre,
        "cargo": cargo,
        "competencia_tipo": tipo_competencia,
        "competencia_id": competencia_id
    }

    dirigentes.append(dirigente)
    cf.escribir_json(RUTA_DIRIGENTES, dirigentes)
    print("✅ Dirigente registrado")
    sc.pausar()

def listar_dirigentes():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA_DIRIGENTES)
    print("\n--- LISTADO DE DIRIGENTES ---")
    for d in dirigentes:
        print(f"ID: {d['id']} | Nombre: {d['nombre']} | Cargo: {d['cargo']} | {d['competencia_tipo'].capitalize()}: {d['competencia_id']}")
    sc.pausar()

def actualizar_dirigente():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA_DIRIGENTES)
    id_dir = input("ID del dirigente a actualizar: ").upper()
    for i, d in enumerate(dirigentes):
        if d["id"] == id_dir:
            nombre = vd.validatetext("Nuevo nombre: ").title()
            cargo = vd.validatetext("Nuevo cargo: ").title()
            tipo = input("Nuevo tipo (liga/torneo): ").lower()
            if tipo not in ["liga", "torneo"]:
                print("❌ Tipo inválido")
                sc.pausar()
                return
            comp_id = input(f"ID de la nueva {tipo}: ").upper()
            datos = cf.leer_json(RUTA_LIGAS if tipo == "liga" else RUTA_TORNEOS)
            if not any(x["id"] == comp_id for x in datos):
                print("❌ No se encontró la competencia")
                sc.pausar()
                return

            dirigentes[i] = {
                "id": id_dir,
                "nombre": nombre,
                "cargo": cargo,
                "competencia_tipo": tipo,
                "competencia_id": comp_id
            }
            cf.escribir_json(RUTA_DIRIGENTES, dirigentes)
            print("✅ Dirigente actualizado")
            break
    else:
        print("❌ Dirigente no encontrado")
    sc.pausar()

def eliminar_dirigente():
    sc.limpiar_pantalla()
    dirigentes = cf.leer_json(RUTA_DIRIGENTES)
    id_dir = input("ID del dirigente a eliminar: ").upper()
    for i, d in enumerate(dirigentes):
        if d["id"] == id_dir:
            del dirigentes[i]
            cf.escribir_json(RUTA_DIRIGENTES, dirigentes)
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
        if op == "1": registrar_dirigente()
        elif op == "2": listar_dirigentes()
        elif op == "3": actualizar_dirigente()
        elif op == "4": eliminar_dirigente()
        elif op == "0": break
        else: print("Opción inválida")
