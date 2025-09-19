try:
    import sqlite3 
    import os
except ImportError as e :
    print('Error al importa  la libreria-->', e)
#Directorio de trabajo actcual
cwd = os.getcwd()

#carpeta donde se guardara la base de datos sqlite3
folder_db = "folder_db"
path_directory =cwd + "python/"

# path_directory = cwd + 
print(cwd)