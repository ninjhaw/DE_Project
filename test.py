from sqlalchemy import create_engine
import pandas as pd
import psycopg2, json, time, schedule
from ftplib import FTP_TLS
from os import environ
from pathlib import Path


def get_ftp() -> FTP_TLS:
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]
    
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()
    return ftp

def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

if __name__ == "__main__":
    get_ftp()
    
    