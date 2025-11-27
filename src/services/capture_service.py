from src.db import get_db



class Capture_service:

    # METODO CREATE
    def create_capture(self, data):
        try: 
            trainer_id = data.get("trainer_id")
            pokemon_id = data.get("pokemon_id")

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO captures(trainer_id, pokemon_id)
                        VALUES (%s,%s) RETURNING id;
                        """, (trainer_id, pokemon_id))
            
            new_id = cur.fetchone()

            conn.commit()
            cur.close()
            conn.close()

            return new_id

        except Exception as e:
            print ("Error crear capture", e)
            return None


capture_service = Capture_service()