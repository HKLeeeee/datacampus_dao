from sqlalchemy import create_engine
import pymysql
import pandas as pd

def connect_db():
    endpoint = 'dao.c51deksujiip.ap-northeast-2.rds.amazonaws.com'
    schema_name = 'storage'
    db_connection_str = 'mysql+pymysql://admin:ekfkawnl@{}/{}'.format(endpoint, schema_name)
    try:
        db_connection = create_engine(db_connection_str)
        conn = db_connection.connect()
    except:
        print('fail to connect db')

    return db_connection

def load_data_from_rds(tabel_name, db_connection):
  sql = "SELECT * FROM {}".format(tabel_name)
  df = pd.read_sql(sql, db_connection)
  return df

def upload_data_to_rds(df, tabel_name, db_connection) :
    df.to_sql(tabel_name, con=db_connection, if_exists='replace', index=False)
