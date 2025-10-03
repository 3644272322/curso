try:
    import os
    from core import config
    import pandas as pd 
except IndexError as e:
    print('error al import la libreria -->',  e)


def create_excel(data, colums):
    #crear la carpeta donde guardaremos el excel si no existe
    if not os.path.exists(config.directory_folder_excel):
        os.makedirs(config.directory_folder_excel)
    
    # crear un dataFrame q es similar a una tabla
    # cuenta con filas u columnas   
    # pd.DataFrame(datas_a_cargar,  nombres_de_las_columnas)
    excel_file = pd.DataFrame(data, colums)
    
    # creaer un archivo excel 
    excel_file.to_excel(config.path_file_excel, engine='openpyxl')
