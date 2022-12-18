from fastapi import FastAPI

app = FastAPI(title="Practica01", description="Formulario", version="0.1")

@app.get("/ejemplo")
async def ejemplo(nombre:str, apellido:str):

    {"nombre":nombre}
    {"apellido":apellido}



    return {"nombre":nombre, "apellido":apellido}

