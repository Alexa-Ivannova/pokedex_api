from src.db import get_db


class Trainer_service:

    # METODO GET_ALL
    def get_all(self ):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT * FROM trainers;
                        """)
            
            data = cur.fetchall()
            cur.close()
            conn.close()

            return data
        
        except Exception as e:
            print("Error get_all: ", e)
            return None

    # METODO GET_BY:ID

    # METODO CREAR

    def create_trainer(self, data):
        try:
            id = data.get("id")
            name = data.get("name")
            region = data.get("region")

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO trainers(id, name, region)
                        VALUES(%s,%s,%s) RETURNING id;
                        """,(id, name, region))
            new_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            return new_id 
        
        except Exception as e:
            print("Error crear trainer", e)
            return None
        
    # METODO UPDATE
    
    # METODO DELETE 
    
        
trainer_service = Trainer_service()