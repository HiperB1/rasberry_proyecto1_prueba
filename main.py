from fastapi import FastAPI, WebSocket
from RFID_services import leer, escribir
from pydantic import BaseModel

app = FastAPI()

class escribirDTO(BaseModel):
    texto: str

@app.get("/")
async def root():
    return {"message": "Welcome to the RFID API"}

@app.websocket("/scan")
async def webssocketendpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        texto = leer()
        data = await websocket.send_text(texto)
        await websocket.send_text(f"El texto enviado es: {data}")


@app.get("/leer")
async def leerEnd():
    datos = leer()
    return {"status": "lectura exitosa", "datos": datos}

@app.post("/escribir")
async def escribirEnd(datos: escribirDTO):
    datosEs = escribir(datos.texto)
    return {"status": "escritura exitosa", "datos": datosEs}


