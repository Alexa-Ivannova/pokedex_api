from src.db import get_db

# DEPENDENCIA

from datetime import datetime

class Pokemon_service:

    # METODO GET ALL:
    def get_all_pokemon(self):
        try:
            
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT * FROM pokemon ORDER BY id;
                        """)
            all_pokemon = cur.fetchall()
            cur.close()
            conn.close()
            return all_pokemon

        except Exception as e:
            print("Error get all pokemon:", e)
            return None


    # METODO GET BY ID:
    def get_pokemon_by_id(self, id):
        try:

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT * FROM pokemon
                        where id = %s;
                        """, (id,))
            
            pokemon_found = cur.fetchone()
            cur.close()
            conn.close()
            return pokemon_found

        except Exception as e:
            print("Error get pokemon by id: ", e)
            return None

    # METODO GET NAME:
    def get_pokemon_by_name (self, data):
        try:
            name = data.get("name")

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT * FROM pokemon
                        WHERE "name" = %s;
                        """, (name,))
            
            name_pokemon = cur.fetchone()
            
            cur.close()
            conn.close()
            return name_pokemon       

        except Exception as e:
            print("Error busqueda por nombre: ", e)
            return None


    # METODO CREAR:
    def create_pokemon(self, data):
        try:
            name = data.get("name")
            level = data.get("level")
            type_id = data.get("type_id")

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO pokemon(name, level, type_id)
                        VALUES (%s,%s,%s) RETURNING id;
                        """,(name, level, type_id))
            
            new_id = cur.fetchone()[0]

            conn.commit()
            cur.close()
            conn.close()
            return new_id

        except Exception as e:
            print("Error crear pokemon: ", e)
            return None

    # METODO UPDATE:
    def update_pokemon(self, data):

        try: 

            id = data.get("id")
            name = data.get("name")
            level = data.get("level")
            type_id = data.get("type_id") 
            deleted_at = data.get("deleted_at")
            
            conn = get_db()
            cur = conn.cursor()

            if name:
                cur.execute("""
                            UPDATE pokemon SET "name" = %s
                            WHERE id = %s;
                            """, (name, id))
            
            if level:
                cur.execute("""
                            UPDATE pokemon SET level = %s
                            WHERE id = %s;
                            """, (level, id))
                
            if type_id:
                cur.execute("""
                            UPDATE pokemon SET type_id = %s
                            WHERE id = %s;
                            """, (type_id, id))
                
            if deleted_at:
                cur.execute("""
                            UPDATE pokemon SET deleted_at = %s
                            WHERE id = %s;
                            """, (deleted_at, id))
                
            conn.commit()
            cur.close()
            conn.close()

            id_pokemon_return = self.get_pokemon_by_id(id)
            return id_pokemon_return
        
        except Exception as e:
            print("Error update: ", e)
            return None

    # METODO DELETE:
    def delete_pokemon(self, id):
        try:

            data ={
                "id": id,
                "deleted_at": datetime.now()
            }

            self.update_pokemon(data)

        except Exception as e:
            print("Error delete pokemon: ", e)
            return None

pokemon_service = Pokemon_service()