# intetamos importamos importar el modulo sqlite3, que nos permite trabajarcon base de datos SQLite
try:  
    import sqlite3 as sql
    import os
    from pathlib import Path
    from core import config
except ImportError as e:
# si ocurre un error al importar,mostramos un mesanje con el detalle del error
    print("Error al importar el modulo: ",e)

# Establecemos una conexion a la base de datos llamada 'database.db.
# si el archivo no existe, SQLite lo crea automáticamente.
conn = sql.connect(config.full_path_file_db)

# ejecutar comandos SQL en la base de datos
cr = conn.cursor()

# crear la tabla 'students' si no existe
cr.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# guardar los cambios en la base de datos
conn.commit()
# consulta para insertar datos
insert_query = "INSERT INTO students (name) VALUES (?)"
val = [
    ('john Doe'),
    ('jane smith'),
    ('Alice johnson'),
    ('Bob Brown'),
]
# insertar datos en la tabla 'students'
# cr.execute(insert_query, val)
cr.execute("INSERT INTO students (name) VALUES ('Adrian')")

# mostrar los datos de la base de datos
rows = cr.execute("SELECT id, name FROM  students").fetchmany
print(rows)

for row in rows:
    print(row)


conn.commit()
# mostrar el número de registros insertados
print(f"{cr.rowcount}registros insertados.")
# cerrar la conxeión a la base de datos 
# conn.close()

