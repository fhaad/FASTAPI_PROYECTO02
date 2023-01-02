from fastapi import FastAPI
import pandas as pd
#---------------------------------------------------------------------------#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///../DB_Database/dataset_new.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#---------------------------------------------------------------------------#

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

'''
En el primer ejemplo damos datos a campos y nos devolvera lo escrito en formato json
'''
@app.get("/ejemplo")
async def ejemplo(nombres:str, apellidos:str, cellphone:str):

    #{"nombre":nombre}
    #{"apellido":apellido}



    return {"nombre":str(nombres), "apellido":str(apellidos), "celular":str(cellphone)}
'''
En el siguiente ejemplo se mostrara el valor de la base de datos
'''
@app.get("/usuarios")
async def users():

    user_list = list(user_db.values())



    return user_list

'''
En este codigo de ejemplo escribiremos el username y nos devuleve la informacion del usuario
'''
@app.get("/usuarios_nombre/{username}")
async def usuarios(username:str):

    
    return user_db[username]

'''
En este ejemplo utilizaremos la expresion Limit para llamar la cantidad de usuarios que debe mostrar
'''
@app.get("/usuarios_consulta")
async def users_query(limit:int):

    user_list = list(user_db.values())


    return user_list[:limit]
'''
En este codigo utilizaremos el campo location para que muestre los registros que contenga esa misma location
'''
@app.get("/usuarios_location/{location}")
async def users_query2(location:str):

    
    return user_db[location]

'''
'''
@app.get("/Base_datos")
async def BaseDatos():
    
    engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

    query = f"SELECT * FROM dataset_new" 
    df = pd.read_sql(sql=query, con=engine)


    return df.to_dict(orient="records")