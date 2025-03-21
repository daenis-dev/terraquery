import json
import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from base_queries import BASE_QUERIES

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()

def test_query(query):
    try:
        cur.execute(query["sql"])
        result = cur.fetchall()
        if len(result) > 0:
            print(f"Query '{query['natural-language']}' returned {len(result)} results.")
            return True
        else:
            print(f"Query '{query['natural-language']}' returned no results.")
            return False
    except Exception as e:
        conn.rollback()
        print(f"Error executing query '{query['natural-language']}': {str(e)}")
        return False

for query in BASE_QUERIES:
    test_query(query)

cur.close()
conn.close()