from fastapi import FastAPI
from os import environ
from sqlalchemy import create_engine
from rapidfuzz import fuzz
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
    """Get the ofac_cons_consolidated

    Returns:
        pd.DataFrame: Returns a dataframe with selected column in the created query
    """
    
    # Get postgresql environment variables
    db = [environ['DB_HOST'], environ['DB_NAME'], environ['DB_USER'], environ['DB_PASS'], environ['DB_PORT'] ]
    db_host, db_name, db_user, db_pass, db_port = db
    
    # engine to connect to postgre
    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')
    
    # load table from SQL
    df = pd.read_sql("SELECT * FROM  ofac_cons_consolidated", con=engine)
    
    return df


# name transformation
def standardize_name(name: str) -> str:
    """Create and format the name in the set standard.

    Args:
        name (str): Value of the name in the column

    Returns:
        str: The standardized name
    """
    clean_name = re.sub('[,]', ' ', name).upper()
    clean_name = re.sub("[^A-Z0-9\\s]", "", clean_name)
    clean_name = re.sub("\\s+", " ", clean_name)    
    return clean_name
    

def get_ratio(s1: str, s2: str, sort_names: bool = False) -> float | None:
    """Calculate the ration of the two strings_

    Args:
        s1 (str): First string
        s2 (str): Second String
        sort_names (bool, optional): . Defaults to False.

    Returns:
        float | None: Returns the ratio of the compared string else returns None
    """
    if sort_names:
        s1 = " ".join(sorted(s1.split()))
        s2 = " ".join(sorted(s2.split()))
    
    # return None on error
    try:
        return round(fuzz.ratio(s1, s2)/100, 4)
    except:
        return None

# Screening app for fastpi
@app.get('/screen/')
async def screen(name: str, threshold: float=0.7) -> dict:
    cleaned_name = standardize_name(name)
    sanctions = get_consolidated()
    
    
    sanctions['similiratiy_score'] = sanctions['cleaned_names'].apply(get_ratio, args=(cleaned_name,))
    sanctions_filtered = sanctions[sanctions['similiratiy_score'] >= threshold]
    
    response = sanctions_filtered.fillna("-").to_dict(orient="records")
    return {
        "status": "success",
        "response": response
    }
        
# home route
@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/users/{user_id}")
# async def get_user_id(user_id: int) -> dict[str, int]:
#     return {"user_id": user_id}


