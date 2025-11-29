from src.db import get_db
from datetime import datetime

class Capture_service:

    # GET ALL 
    def get_all_captures(self):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT c."id" AS "id_capturas", t."name" AS "name_trainer", p."name" AS "name_pokemon", p."level" AS "level_pokemon", ty."name" AS "name_type", c."capturated_at" AS "captured_date"
		                FROM captures c
                        INNER JOIN trainers t on t.id = c.trainer_id 
                        INNER JOIN pokemon p on p.id = c.pokemon_id 
                        INNER JOIN "types" ty on ty.id  = p.type_id;
                        """)
            
            data_get_all_capture = cur.fetchall()
            cur.close()
            conn.close()
            return data_get_all_capture

        except Exception as e:
            print("Error get all captures: ", e)
            return None
        
    # GET CAPTURE BY ID
    def get_capture_by_id(self,id):
        try:

            conn = get_db()
            cur = conn.cursor()

            cur.execute("""
                        select * from captures
                        where id = %s;    
                        """,(id,))
            id_capture = cur.fetchone()
            cur.close()
            conn.close()
            return id_capture
        
        except Exception as e:
            print("Error get capture by id: ", e)
            return None

    # GET BY TRAINER ID CAPTURE:
    def get_by_trainer_id_capture(self, id):
        try: 
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        select t."id" as "id_trainer", c."id" as "id_capture", t."name" as "name_trainer", 
		                p."name" as "name_pokemon", p."level" as "level_pokemon",
		                ty."name" as "type_pokemon",
		                c."capturated_at" as "date_capture"
		                from captures c
		                inner join trainers t on t.id = c.trainer_id
		                inner join pokemon p  on p.id = c.pokemon_id
		                inner join "types" ty on ty.id = p.type_id
                        where t.id = %s;
                        """, (id,))
            
            new_id = cur.fetchall()
            cur.close()
            conn.close()
            return new_id

        except Exception as e:
            print("Error get_ny_id: ", e)
            return None
        
    # GET BY POKEMON ID CAPTURE:
    def get_by_pokemon_id_capture(self, id):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        select  c."id" as "id_capture",
                        p."id" as "id_pokemon", p."name" as "name_pokemon", 
		                t."name" as "name_trainer",
                        ty."name" as "type_pokemon", 
                        p."level" as "pokemon_level",
                        c."capturated_at" as "data_capture"
                        from captures c 
                        inner join pokemon p on p.id = c.pokemon_id 
                        inner join trainers t  on t.id = c.trainer_id 
                        inner join "types" ty on ty.id  = p.type_id 
                        where p.id = %s;
                        """, (id,))
            
            captures_pokemon_id = cur.fetchall()
            cur.close()
            conn.close()
            return captures_pokemon_id
        
        except Exception as e:
            print("Error get by pokemon: ", e)
            return None

    # GET MATCH BY TRAINER AND POKEMON EXISTE ENTRENADOR CON ESE POKEMON
    def get_match_trainer_and_pokemon_capture(self,data):
        try: 
            trainer_id =  data.get("trainer_id")
            pokemon_id = data.get("pokemon_id")

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT * from captures 
                        where trainer_id = %s
                        and pokemon_id = %s;
                        """, (trainer_id, pokemon_id))
            
            new_match = cur.fetchone()
            print("new match: ", new_match)

            cur.close()
            conn.close()
            return new_match

        except Exception as e:
            print("Error get by id capture; ", e)
            return None
        


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

    #METODO ACTUALIZAR CAPTURA
    def update_capture(self,data):
        try: 
            id = data.get("id")
            trainer_id = data.get("trainer_id")
            pokemon_id = data.get("pokemon_id")
            capturated_at = data.get("capturated_at")
            freed_at = data.get("freed_at")

            conn = get_db()
            cur = conn.cursor()

            if trainer_id:
                cur.execute("""
                            UPDATE captures SET trainer_id = %s
                            WHERE id = %s;
                            """, (trainer_id, id))
                
            if pokemon_id:
                cur.execute("""
                            UPDATE captures SET pokemon_id = %s
                            WHERE id = %s;
                            """, (pokemon_id, id))

            if capturated_at:
                cur.execute("""
                            UPDATE captures SET capturated_at = %s
                            WHERE id = %s;
                            """, (capturated_at, id))
                
            if freed_at:
                cur.execute("""
                            UPDATE captures SET freed_at = %s
                            WHERE id = %s;
                            """, (freed_at, id))
                
            conn.commit()
            cur.close()
            conn.close()

            id_capture_return = self.get_capture_by_id(id)
            return id_capture_return  
        
        except Exception as e:
            print("Error update capture: ", e)
            return None
        
    # METODO DELETE CAPTURE
    def delete_capture(self, id):
        try:

            data ={
                "id": id,
                "freed_at": datetime.now()
                }
            
            self.update_capture(data)

        except Exception as e:
            print("Error delete", e)
            return None

capture_service = Capture_service()