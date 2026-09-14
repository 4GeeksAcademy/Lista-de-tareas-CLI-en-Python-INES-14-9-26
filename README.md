# Lista-de-tareas-CLI-en-Python-INES-14-9-26

Herramienta ligera de terminal para que el equipo de operaciones registre,
consulte y elimine tareas pendientes, en lugar de anotarlas entre mensajes
de chat o notas sueltas.

## Uso

Requiere Python 3.

```bash
python3 todo.py
```

Se muestra un menu con estas opciones:

1. **Agregar tarea**: pide un titulo y la agrega a la lista.
2. **Mostrar tareas**: lista todas las tareas pendientes con su posicion
   numerica (1, 2, 3, ...).
3. **Eliminar tarea**: muestra la lista y pide la posicion de la tarea a
   eliminar. No permite editar tareas: si hay un error, se elimina y se
   vuelve a crear con el titulo correcto.
4. **Salir**: cierra el programa.

## Persistencia

Las tareas se guardan automaticamente en `todos.csv` (en la misma carpeta)
cada vez que se agrega o elimina una tarea, y se cargan de nuevo al iniciar
el programa. Esto permite cerrar y abrir la terminal durante el dia sin
perder el progreso.

`todos.csv` no se sube al repositorio (ver `.gitignore`), ya que es el
archivo de datos local de cada persona que usa la herramienta.
