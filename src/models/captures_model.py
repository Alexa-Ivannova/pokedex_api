from src.db import get_db

def captures_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS captures(
                    id SERIAL PRIMARY KEY,
                    trainer_id VARCHAR(50) REFERENCES trainers(id) ON DELETE CASCADE,
                    pokemon_id INT REFERENCES pokemon(id) ON DELETE CASCADE,
                    capturated_at TIMESTAMP DEFAULT NOW(),
                    freed_at TIMESTAMP
                    );
                    """)
        
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print("Error al iniciar la base de datos", e)