import pandas as pd
import psycopg2, json, time, schedule
from ftplib import FTP_TLS
from os import environ, remove
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

def delete_files(file_source: Path):
    remove(file_source)
    
def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

def pipeline():
    # Load source configuration
    with open("config.json", "rb") as file:
        config = json.load(file)
        
    ftp = get_ftp()
    
    # Loop through each config to get source_name 
    for source_name, source_config in config.items():
        filename = Path(source_name + '.CSV')
        df = read_csv(source_config)
        df.to_csv(filename, index=False)
        print(f"{filename} has been downloaded to the directory.")
        
        print(f"Uploading {filename} to FTP Server. ")
        time.sleep(1)
        upload_to_ftp(ftp, filename)
        print(f"{filename} has been uploaded to FTP server")
        
        print(f"Deleting {filename} from local files.")
        delete_files(filename)
        print(f"{filename} has been deleted from the local files\n")


if __name__ == "__main__":
    
    schedule.every().day.at("22:30").do(pipeline)
    
    while True:
        schedule.run_pending()
        time.sleep(1)