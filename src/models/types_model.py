from src.db import get_db

def types_db():
    try: 
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS types (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT NOW()
                    );
                    """)
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print("Error al iniciar la BD", e)