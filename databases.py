import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@127.0.0.1:5432/database')

query = """select * from table"""
df = pd.read_sql_query(query, con=engine)
