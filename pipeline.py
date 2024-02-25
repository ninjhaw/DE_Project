from logging import config
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

def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as file:
        ftp.storbinary(f"STOR {file_source.name}", file)

def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

def pipeline():
    ftp = get_ftp()
    with open("config.json", "rb") as file:
        config = json.load(file)
        
    for source_name, source_config in config.items():
        filename = Path(f'datasets/{source_name}.csv')
        df = read_csv(source_config)
        df.to_csv(filename, index=False)
        print(f"Downloaded {source_name}.")
        
        upload_to_ftp(ftp, filename)
        print(f"{source_name} uploaded to FTP Server..")
    
    

if __name__ == "__main__":
    
    schedule.every().day.at("23:32").do(pipeline)
    
    while 1:
        schedule.run_pending()
        time.sleep(1)
    