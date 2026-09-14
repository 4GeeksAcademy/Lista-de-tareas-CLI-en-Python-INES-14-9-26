#!/usr/bin/env python3
"""
Lista de tareas CLI
====================

Herramienta ligera de terminal para que los coordinadores operativos
registren, consulten y eliminen tareas pendientes, sin depender de
mensajes de chat o notas sueltas.

Las tareas se guardan automaticamente en un archivo local (todos.csv)
cada vez que se agrega o elimina una tarea, y se cargan al iniciar el
programa. Esto permite cerrar y abrir la terminal durante el dia sin
perder el progreso.
"""

import csv
import os

TASKS_FILE = "todos.csv"

# Lista de tareas en memoria. Todas las funciones de este modulo la leen
# y modifican directamente, en vez de recibirla como parametro.
tasks = []


def load_todos(path=TASKS_FILE):
    """Carga las tareas guardadas en el archivo CSV a la lista en memoria.

    Si el archivo no existe todavia (primer uso), deja la lista vacia
    en lugar de fallar.
    """
    tasks.clear()
    if not os.path.exists(path):
        return

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                tasks.append(row[0])


def save_todos(path=TASKS_FILE):
    """Guarda la lista de tareas en memoria en el archivo CSV, una por fila."""
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])


def add_one_task(title):
    """Agrega una tarea nueva a la lista en memoria, por su titulo.

    Valida que el titulo no este vacio. Devuelve True si se agrego,
    False en caso contrario.
    """
    title = title.strip()
    if not title:
        print("El titulo de la tarea no puede estar vacio.")
        return False
    tasks.append(title)
    print(f'Tarea agregada: "{title}"')
    return True


def print_list():
    """Muestra todas las tareas pendientes en memoria con su posicion numerica."""
    if not tasks:
        print("No hay tareas pendientes.")
        return

    print("\nTareas pendientes:")
    for position, task in enumerate(tasks, start=1):
        print(f"  {position}. {task}")
    print()


def delete_task(number_to_delete):
    """Elimina de la lista en memoria la tarea en la posicion indicada (1-based).

    Devuelve True si se elimino correctamente, False si la posicion
    no era valida.
    """
    if not tasks:
        print("No hay tareas para eliminar.")
        return False

    if number_to_delete < 1 or number_to_delete > len(tasks):
        print(f"Posicion invalida. Debe estar entre 1 y {len(tasks)}.")
        return False

    removed = tasks.pop(number_to_delete - 1)
    print(f'Tarea eliminada: "{removed}"')
    return True


def ask_int(prompt):
    """Pide un numero entero al usuario. Devuelve None si no es valido."""
    value = input(prompt).strip()
    try:
        return int(value)
    except ValueError:
        return None


def show_menu():
    print("=" * 40)
    print("  Lista de tareas - equipo de operaciones")
    print("=" * 40)
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")


def main():
    load_todos()
    print(f"Se cargaron {len(tasks)} tarea(s) desde {TASKS_FILE}.")

    while True:
        show_menu()
        option = input("Elegi una opcion (1-4): ").strip()

        if option == "1":
            title = input("Titulo de la nueva tarea: ")
            if add_one_task(title):
                save_todos()

        elif option == "2":
            print_list()

        elif option == "3":
            print_list()
            if tasks:
                position = ask_int("Posicion de la tarea a eliminar: ")
                if position is None:
                    print("Ingresa un numero valido.")
                elif delete_task(position):
                    save_todos()

        elif option == "4":
            print("Tareas guardadas. Hasta pronto.")
            break

        else:
            print("Opcion invalida. Elegi un numero del 1 al 4.")

        print()


if __name__ == "__main__":
    main()
