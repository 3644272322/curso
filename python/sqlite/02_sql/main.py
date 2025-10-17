from core import confing
from db import manager
confing.create_dir()
manager.DBManager(confing.NAME_DB)