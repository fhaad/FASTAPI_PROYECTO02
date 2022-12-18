from fastapi import FastAPI
import pandas as pd
import sqlalchemy as sql
from sqlalchemy import engine

app = FastAPI(title="Practica01", description="Formulario", version="0.1")

database_ubicacion = "sqlite:///../DB_Database/dataset_new.db"

# Se crea una pequeña base de datos en un diccionario
user_db = { 

    'jack':{'username':'jack', 'dated_joined':'2022-01-01', 'location':'New York', 'age':'28'},
    'joe':{'username':'joe', 'dated_joined':'2022-02-01', 'location':'Memphis', 'age':'25'},
    'jane':{'username':'jane', 'dated_joined':'2022-03-01', 'location':'Miami', 'age':'30'},
    'peter':{'username':'peter', 'dated_joined':'2022-01-01', 'location':'New York', 'age':'32'},
    'jhon':{'username':'jhon', 'dated_joined':'2022-02-01', 'location':'Memphis', 'age':'29'},
    'dina':{'username':'dina', 'dated_joined':'2022-03-01', 'location':'Miami', 'age':'26'}
}


@app.get("/ejemplo")
async def ejemplo(nombres:str, apellidos:str, cellphone:str):

    #{"nombre":nombre}
    #{"apellido":apellido}



    return {"nombre":str(nombres), "apellido":str(apellidos), "celular":str(cellphone)}
'''

'''
@app.get("/usuarios")
async def users():

    user_list = list(user_db.values())



    return user_list

'''
'''
@app.get("/usuarios_nombre/{username}")
async def usuarios(username:str):

    
    return user_db[username]

'''
'''
@app.get("/usuarios_consulta")
async def users_query(limit:int):

    user_list = list(user_db.values())



    return user_list[:limit]
'''
'''

@app.get("/Base_datos")
async def BaseDatos():
    
    engine = sql.create_engine(url = database_ubicacion)

    query = f"SELECT * FROM dataset_new" 
    df = pd.read_sql(sql=query, con=engine)


    return df.to_dict(orient="records")