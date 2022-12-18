from fastapi import FastAPI, Query
import pandas as pd
import sqlalchemy as sql
from sqlalchemy import engine
from pydantic import Required


# mensaje
database_ubicacion = "sqlite:///../DB_Database/dataset_new.db"

app = FastAPI (title="Proyecto_02 Federico", description="ETL", version="0.1")

@app.get("/Aplication1")

async def consulta1(platform:str, type:str, year:int):

    # Aqui se realiza la conexion a la base de datos
    engine = sql.create_engine(url = sqlalchemy_database)
    df = pd.read_sql('dataset_new', engine)

    # Linea de solicitud
    consulta = (df['platform'] == platform) & (df['release_year'] == year) & (df['type'] == type)
    resultado = df[consulta]['min'].idxmax()


    

    return df.loc[resultado, 'title']
'''

'''
@app.get("/Aplication2")

#async def consulta2(platform:str, type:str, platform1:str, type1:str):
async def consulta2(platform:str):

    
    engine = sql.create_engine(url = sqlalchemy_database)
    df = pd.read_sql('dataset_new', engine)


    
    consulta5 = (df['platform'] == platform)
    peliculas = df[consulta5]['type'].str.contains('Movie').sum()
    series = df[consulta5]['type'].str.contains('TV Show').sum()

    return {"Pelis":int(peliculas), "Series":int(series)}

'''

'''
@app.get("/Aplication3")

async def consulta3(genero:str):

    
    engine = sql.create_engine(url = sqlalchemy_database)
    df = pd.read_sql('dataset_new', engine)


    #consulta = (df['platform'] == platform) & (df['release_year'] == year) & (df['type'] == type)
    #resultado = df[consulta]['min'].idxmax()
    consulta6 = df['listed_in'].str.contains(genero)
    Ngenero = df[consulta6].groupby('platform')['listed_in'].count()
    return Ngenero.to_dict()

'''

'''
@app.get("/Aplication4")

async def consulta4(year:int, platform:str):

    
    engine = sql.create_engine(url = sqlalchemy_database)
    df = pd.read_sql('dataset_new', engine)


    consulta7 = (df['platform']==platform)&(df['release_year']==year)
    act = df[consulta7]['cast'].str.split(pat = ',', expand=True)
    un = pd.concat(objs = [act[i] for i in range(len(act.columns))], ignore_index=True)
    todo = un.value_counts().to_dict()
    return list(todo.items())[0]
    
    #consulta = (df['platform'] == platform) & (df['release_year'] == year) & (df['type'] == type)
    #resultado = df[consulta]['min'].idxmax()
    #consulta6 = df['listed_in'].str.contains(genero)
    #Ngenero = df[consulta6].groupby('platform')['listed_in'].count()
    #return Ngenero.to_dict()

    
