import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/northwind')

pd.read_sql('SELECT * FROM customers')

