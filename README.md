# 📂 Gestor de Torneo de Fútbol

Este proyecto es un **sistema de gestión de torneos de fútbol** desarrollado en Python, con enfoque en la gestión local y remota de entidades como jugadores, equipos, dirigentes, ligas, torneos, partidos, transferencias y estadísticas.

El sistema utiliza archivos JSON como almacenamiento persistente y está estructurado en módulos separados con una arquitectura organizada para facilitar su mantenimiento, escalabilidad y claridad de código.

---

## 🎯 Objetivos del sistema

* Registrar y administrar **equipos** y sus datos básicos.
* Agregar y gestionar **jugadores** por equipo.
* Registrar y listar **dirigentes** (entrenadores, presidentes, etc.).
* Administrar **ligas locales** y **torneos internacionales**.
* Controlar el calendario y resultados de **partidos**.
* Gestionar **transferencias de jugadores** entre equipos.
* Generar **estadísticas** de edad y goles anotados.

---

## 🧱 Estructura del Proyecto

```
torneo_futbol/
│
├── app/
│   └── main.py                      # Punto de entrada del programa
│
├── controllers/                    # Módulos funcionales
│   ├── equipos.py                  # CRUD de equipos
│   ├── jugadores.py                # CRUD de jugadores
│   ├── dirigentes.py               # CRUD de dirigentes
│   ├── ligas.py                    # CRUD de ligas locales
│   ├── torneos.py                  # CRUD de torneos internacionales
│   ├── partidos.py                 # CRUD de partidos
│   ├── transferencias.py           # Módulo de compra/préstamo de jugadores
│   └── estadisticas.py             # Análisis estadístico
│
├── utils/                          # Utilidades auxiliares
│   ├── corefiles.py                # Lectura y escritura de archivos JSON
│   ├── screenControllers.py        # Limpieza y pausa de pantalla
│   └── validateData.py             # Validación de entradas por consola
│
├── data/                           # Base de datos en JSON
│   ├── equipos.json
│   ├── jugadores.json
│   ├── dirigentes.json
│   ├── ligas.json
│   ├── torneos.json
│   ├── partidos.json
│   └── transferencias.json
```

---

## 🔄 CRUD implementado por módulo

### 📘 Equipos

* ID automático (`EQ001`, `EQ002`...)
* Nombre, país, fecha de fundación, ID de liga
* Asociado a jugadores y dirigentes

### 👥 Jugadores

* ID automático (`JUG001`...)
* Nombre, dorsal, posición, fecha nacimiento, ID equipo

### 🎩 Dirigentes

* ID automático (`DI001`...)
* Nombre, cargo (DT, presidente, etc.), equipo asignado

### 🏆 Torneos (Internacionales)

* ID automático (`TR001`...)
* País, fecha inicio y fin

### 🏟️ Ligas (Locales)

* ID automático (`LIG001`...)
* Nombre, país, fechas de inicio y fin

### 🗓️ Partidos

* Registro de resultado entre equipos
* Goles por equipo, torneo asociado, fecha

### 🔄 Transferencias

* Simula compra o préstamo
* Solicitud con valor ofrecido, confirmación manual
* Actualiza equipo del jugador y guarda historial

### 📊 Estadísticas

* Jugador más joven
* Jugador más veterano
* Total de goles en todos los partidos

---

## ⚙️ Requisitos del Sistema

* Python 3.8 o superior
* Compatible con **Windows** y **Linux**
* No requiere librerías externas

---

## ▶️ Ejecución del sistema

Ejecuta el archivo `main.py` desde la terminal:

```bash
cd app
python main.py
```

El menú principal te permitirá acceder a cada módulo del sistema:

* Gestión de jugadores, equipos, partidos
* Análisis de estadísticas
* Transferencias de jugadores

---

## 🧠 Buenas prácticas usadas

* Diccionarios planos con claves claras (`id`, `nombre`, `equipo_id`, etc.)
* Archivos `.json` organizados por entidad
* Módulos separados por responsabilidad (principio SOLID)
* Validación de entradas para evitar errores en consola
* Interfaz por consola limpia y clara

---

## 👩‍💻 Autor

Proyecto desarrollado por **María Alejandra García** – 2025. Todos los derechos reservados. 💙⚽
Camper 2025
