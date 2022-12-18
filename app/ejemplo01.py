from fastapi import FastAPI

app = FastAPI(title="Practica01", description="Formulario", version="0.1")

user_db = { 

    'jack':{'username':'jack', 'dated_joined':'2022-01-01', 'location':'New York', 'age':'28'},
    'joe':{'username':'joe', 'dated_joined':'2022-02-01', 'location':'Memphis', 'age':'25'},
    'jane':{'username':'jane', 'dated_joined':'2022-03-01', 'location':'Miami', 'age':'30'}


}


@app.get("/ejemplo")
async def ejemplo(nombres:str, apellidos:str, cellphone:str):

    #{"nombre":nombre}
    #{"apellido":apellido}



    return {"nombre":str(nombres), "apellido":str(apellidos), "celular":str(cellphone)}

