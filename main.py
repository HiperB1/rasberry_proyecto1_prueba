from fastapi import FastAPI
from leer import leer, escribir
from pydantic import BaseModel

app = FastAPI()

class escribirDTO(BaseModel):
    texto: str

@app.get("/")
async def root():
    return {"message": "Welcome to the RFID API"}

@app.get("/leer")
async def leerEnd():
    datos = leer()
    return {"status": "lectura exitosa", "datos": datos}

@app.post("/escribir")
async def escribirEnd(datos: escribirDTO):
    datos = escribir(datos.texto)
    return {"status": "escritura exitosa", "datos": datos.texto}


