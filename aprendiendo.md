# Aprendiendo con este proyecto

Notas propias sobre como esta armado `todo.py`: que estructuras de datos usa
realmente y los pasos que se siguieron para construirlo.

## Aclaracion importante: no se usan diccionarios

Revisando el codigo, **no hay ningun `dict` en este proyecto**. La estructura
central es una **lista** de Python:

```python
tasks = []
```

Cada tarea es simplemente un `string` (el titulo) guardado como un elemento
de esa lista. Por que una lista y no un diccionario:

- Las tareas se referencian por **posicion** (1, 2, 3...), no por una clave
  con nombre. Una lista ya tiene ese orden y esa indexacion "gratis"
  (`tasks[0]` es la tarea 1, etc.), mientras que un diccionario no garantiza
  orden de forma tan directa para este caso de uso.
- Eliminar por posicion es literalmente `tasks.pop(posicion - 1)`.
- Guardar/cargar en CSV es directo: una fila = un elemento de la lista.

Si mas adelante cada tarea necesitara mas de un dato (por ejemplo titulo +
fecha + responsable), ahi si tendria sentido pasar cada tarea a un
diccionario, por ejemplo `{"titulo": ..., "fecha": ...}`, y `tasks` pasaria a
ser una lista de diccionarios. Pero en esta version, con solo el titulo,
alcanza y sobra con strings dentro de una lista.

### Otras estructuras/herramientas usadas

- `list` (`tasks`): la lista en memoria con todas las tareas pendientes.
- Modulo `csv` (estandar de Python): para leer y escribir `todos.csv` fila
  por fila (`csv.reader`, `csv.writer`), en vez de partir el texto a mano
  por comas (eso evita romperse con titulos que ya tienen comas o comillas).
- Modulo `os` (estandar de Python): solo para `os.path.exists(...)`, y asi
  no fallar si `todos.csv` todavia no existe la primera vez que se corre.
- `input()` / `print()`: toda la interaccion por terminal, sin librerias
  externas de CLI (nada de `argparse`, `click`, etc. porque no hacian falta
  para un menu simple).

## Paso a paso de como se armo el proyecto

1. **Punto de partida**: un repo vacio con solo un `README.md`.

2. **Brief funcional**: el PM pidio una CLI para agregar tareas, listarlas
   con posicion numerica, eliminarlas por posicion, y guardarlas/cargarlas
   de un archivo `todos.csv`. Explicitamente, sin edicion: para corregir
   algo se elimina y se vuelve a crear.

3. **Primera version funcional** (`todo.py`): un menu en un `while True`
   con 4 opciones (Agregar / Mostrar / Eliminar / Salir), y funciones que
   al principio recibian la lista de tareas como parametro
   (`agregar_tarea(tareas, titulo)`, etc.), con nombres en español.

4. **Persistencia**: se agrego lectura/escritura de `todos.csv` con el
   modulo `csv`, cargando al arrancar el programa y guardando automatico
   despues de cada alta o baja (asi nadie pierde tareas si se olvida de
   guardar a mano entre turnos).

5. **Refactor a lista en memoria global**: se cambio el diseño para que las
   funciones no reciban la lista por parametro, sino que operen directo
   sobre una lista a nivel de modulo (`tasks = []`), y se renombraron las
   funciones a ingles, una por una, segun se fueron pidiendo:
   - `add_one_task(title)` - agrega una tarea nueva a `tasks`.
   - `print_list()` - muestra todas las tareas con su posicion (1-based).
   - `delete_task(number_to_delete)` - elimina la tarea en esa posicion.
   - `save_todos()` - escribe `tasks` en `todos.csv`.
   - `load_todos()` - lee `todos.csv` y reconstruye `tasks`.

6. **Verificacion contra los criterios de evaluacion**: para cada funcion
   se probaron casos limite (titulo vacio, posiciones invalidas como 0 o
   fuera de rango, lista vacia, caracteres especiales como comas/comillas/
   tildes en los titulos, y el ciclo completo guardar -> cerrar -> volver a
   cargar) para confirmar que el comportamiento era correcto, sin tener que
   tocar el codigo porque ya cumplia.

7. **Restricciones confirmadas**:
   - Solo se usan modulos de la libreria estandar (`csv`, `os`), nada de
     dependencias externas.
   - No hay ninguna funcion de edicion/actualizacion en sitio: el flujo
     para corregir una tarea es eliminarla y volverla a crear, tal como
     pedia el brief.

8. **Como correrlo**: desde la carpeta del proyecto,

   ```bash
   python3 todo.py
   ```

   Esto abre el menu interactivo en la propia terminal. `todos.csv` se crea
   solo, y no se sube al repositorio (esta en `.gitignore`) porque es el
   archivo de datos local de cada persona que usa la herramienta.
