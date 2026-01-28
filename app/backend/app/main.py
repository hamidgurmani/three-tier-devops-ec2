from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM items;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return {"items": rows}
    except Exception as e:
        return {"error": str(e)}

