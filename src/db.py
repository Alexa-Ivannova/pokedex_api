from dotenv import load_dotenv
import os, psycopg2

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# ABRIR UNA CONECCIÓN EN LA BD
def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn