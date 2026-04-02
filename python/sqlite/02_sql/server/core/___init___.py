try:
    import os 
    from pathlib import Path
except ImportError as e:
    print("Error modulo-->", e )

# otbener del directorio de trabajo actual 
cwd = os.getcwd()
custom_patch = os.path.join(cwd,"python/sqlite/02_sql")

DIR_DB = os.path.join(custom_patch,"db/folder_db")
DIR_EXCEL = os.path.join(custom_patch,"public/excel")


def create_dir():
    for dir in [DIR_DB,DIR_EXCEL]:
        if not os.path.exists(dir):
         os.makedirs(dir)   
# #nombre de la carpeta donde  almacenarmos el archivo.db o la base de datos
# directorio_capeta:db = "db/folder_db"

# trabajando en una computadora local o en un espacio de codigo de github no hacer falta argregar las siguiente variables
# # con solo argregar full_path_db = os.join(cwd.directorio_carpeta_db) 
