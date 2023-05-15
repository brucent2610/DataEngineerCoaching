# TODO: Rebuild the structure
# https://soshace.com/optimizing-database-interactions-in-python-sqlalchemy-best-practices/
# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

import pandas as pd
import sqlalchemy as db
from sqlalchemy import text

engine = db.create_engine("mysql+mysqlconnector://root:root@127.0.0.1:3306/sqlalchemy_mysql")

statement = 'SELECT * FROM posts LIMIT 10'

with engine.connect() as con:
    rs = con.execute(text(statement))

posts_df = pd.read_sql_query(statement, engine)
print(posts_df[["ViewCount", "AnswerCount"]].min())
