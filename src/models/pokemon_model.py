from src.db import get_db

def pokemon_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS pokemon(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    level INT NOT NULL,
                    type_id INT REFERENCES types(id) ON DELETE RESTRICT,
                    created_at TIMESTAMP DEFAULT NOW(),
                    deleted_at TIMESTAMP
                    );
                    """)
        
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print("Error al iniciar la base de datos", e)