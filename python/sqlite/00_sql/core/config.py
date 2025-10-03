try:  
    import os
    from pathlib import Path
except ImportError as e:
# si ocurre un error al importar,mostramos un mesanje con el detalle del error
    print("Error al importar el modulo: ",e)

#obtener el directorio de trabajo actual
cwd = os.getcwd()
print(cwd) 
custom_path = cwd + "/python/sqlite/00_sql"

# nombre de la carpeta donde almasabaremos el archivo .db o la base de datos
directorio_db = "db/folder_db"
# crear la ruta de la carpeta folder_db
full_path_db = os.path.join(custom_path, directorio_db)

# comprobar si la carpeta folder_db ya existe 
# si no existe se crea la carpeta de lo contrario no se crea al carpeta
if not os.path.exists(full_path_db):
    # crear la carpeta 
    os.makedirs(full_path_db)

# crear el archivo de base de datos en las carpeta db/folder_db
nombre_file_db = "test"
# comprobar que el archivo db cuente con el sufijo .db
nombre_file_db = str(Path(nombre_file_db).with_suffix(".db").stem + ".db")
# guardar la base de dato
full_path_file_db = os.path.join(full_path_db,nombre_file_db)
