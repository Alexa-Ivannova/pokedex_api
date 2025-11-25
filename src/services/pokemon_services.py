from src.db import get_db


class Pokemon_service:

    # METODO GET ALL:


    # METODO GET BY ID:

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


    # METODO DELETE:

pokemon_service = Pokemon_service()