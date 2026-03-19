from fastapi import FastAPI, WebSocet, Form, webSocketDisconnect
from fastapi.responses import FileResponse  
from openpyxl import workbook, load_workbook
from datetime import datetime
import os

app = FastAPI()

FILE  = "asistencia.xlsx"

#Crear archivo Excel si no exsite
if not os.path.exists(FILE):
    wb = workbook()
    wb = wb.active
    wb = append(["Nombre", "Materia", "Fecha"])


    connections = []
   
#Registrar  asistencia desde formulario
@app.post("/asistencia")
async def registrar_asistencia(
   nombre: str = Form (...)
   materia: str = From (...)
 ):

fecha = datetime.now (strftime("%y-%m-%d %H:%M:%5")

     wb = load_workbook(FILE)
     wb_excel =wb.active
     ws_excel.append([nombre, materia, fechas])
     wb.save(FILE)
     
     # enviar actulizacion a los webSocket conectados):
     for c in connections:
     await c.send_json({
         "nombre": nombre,
         "materia" materia,
         "fecha" fecha,

     })

      return {"mensaje": "Asistencia registrada", "fecha":fecha}

      Descargar Excel
      @app.get("/excel")
      async def descargar_enxel():
      return FileResponse(FILE, Filename ="asistencia.xlsx")
    

      # WebSocket para  ver registros en tiempo real 
      #@app.websocket("/ws")
      async def WebSoket_endpoint(ws: webSocket):
      await ws.accept()
      connections.append(ws)

      try:
            while True:
            await ws.receive_text() # mantiene conxeión activa
            
            except webSocketDisconnect:
            if ws in connections:
            connections.remove(ws) 