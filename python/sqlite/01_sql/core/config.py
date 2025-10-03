try:
    import os 
    from pathlib import Path    
except ImportError as e:
    print('Error al importar', e)

#obtener el directorio de trabajo actual
cwd = os.getcwd()
custom_path = os.path.join(cwd, "python/sqlite/01_sql")

# nombre de la carpeta donde almasabaremos el archivo .db o la base de datos
directorio_db = "db/folder_db"
# crear la ruta de la carpeta folder_db
full_path_db = os.path.join(custom_path, directorio_db)

# comprobar si la carpeta folder_db ya existe 
# si no existe se crea la carpeta de lo contrario no se crea al carpeta
if not os.path.exists(full_path_db):
#     # crear la carpeta 
    os.makedirs(full_path_db)

# crear el archivo de base de datos en las carpeta db/folder_db
filename_db = "test"
# comprobar que el archivo db cuente con el sufijo .db
filename_db = str(Path(filename_db).with_suffix(".db").stem + ".db")
# guardar la base de dato
full_path_file_db = os.path.join(full_path_db, filename_db)

# nombre de la carpeta donde guardaremos el archivo  excel
directory_excel = './public/excel'
directory_folder_excel = os.path.join((cwd + '/python/sqlite/01_sql'), directory_excel)


# nombre del archivo excel

filename_excel = 'example.xlsx'
# comprobar si tiene el sufigo xlsx
filename_excel = str(Path(filename_excel).with_suffix('.xlsx').stem + '.xlsx')

# crear el archivo axcel en el directorio destino
path_file_excel = os.path.join(directory_folder_excel, filename_excel)