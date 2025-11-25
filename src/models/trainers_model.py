from src.db import get_db

def trainers_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS trainers(
                    id VARCHAR(50) UNIQUE PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    region VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW(),
                    deleted_at TIMESTAMP
                    );
                    """)
        
        conn.commit()
        cur.close()
        conn.close
        
    except Exception as e:
        print("Error al iniciar la base de datos", e)