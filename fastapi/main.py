from typing import Union
from urllib import response
from fastapi import FastAPI, HTTPException
from os import environ
from sqlalchemy import create_engine, Engine, URL
from rapidfuzz import fuzz
from fastapi.responses import ORJSONResponse
import logging, pandas as pd, re

# fastapi app
app = FastAPI()


logging.basicConfig(filename='r_logs.log', level=logging.INFO)
@app.middleware("http")
async def log_requests(request, call_next):
    '''
    Track all the requests & responses and store it to r_logs.log file.
    '''
    
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response: {response.status_code}")
    return response


# helper function
def get_consolidated() -> pd.DataFrame:
    # Get postgresql environment variables
    db_host = environ['DB_HOST']
    db_name = environ['DB_NAME']
    db_user = environ['DB_USER']
    db_pass = environ['DB_PASS']
    db_port = environ['DB_PORT']
    
    # engine to connect to postgre
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')
    
    # load table from SQL
    df = pd.read_sql("SELECT * FROM  ofac_cons_consolidated", con=engine)
    
    return df


# name transformation
def standardize_name():
    ...
    
    

# Screening app for fastpi
@app.get('/screen')
async def screen(name: str, threshold: float=0.7) -> dict:
    df = get_consolidated().head().fillna('-')
    response = df.to_dict(orient="records")
    return {
        "status": "success",
        "response": response
    }        
        
    
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/users/{user_id}")
# async def get_user_id(user_id: int) -> dict[str, int]:
#     return {"user_id": user_id}


