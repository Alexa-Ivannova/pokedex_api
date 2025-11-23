from src.db import get_db


class Trainer_service:
    def create_trainer(self, data):

        # METODO CREAR
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
        
trainer_service = Trainer_service()