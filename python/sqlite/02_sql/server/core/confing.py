try:
    import os
    from pathlib import Path
except ImportError as e:
    print("Error modulo-->",e )

cwd = os.getcwd()
custom_patch = os.path.join(cwd,"")

DIR_DB = os.path.join(custom_patch,"db/folder_db")
DIR_EXCEL = os.path.join(custom_patch,"public/excel")

def create_dir():
    for dir in [DIR_DB, DIR_EXCEL]:
        if not os.path.exists(dir):
            os.makedirs(dir)

NAME_DB = "database"
  