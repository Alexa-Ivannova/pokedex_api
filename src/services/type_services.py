from src.db import get_db


class Type_service: 

    # METODO GET (OBTENER TODOS)
    def get_all():
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT * FROM types ORDER BY id;")
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return rows

        except Exception as e:
            print("Error get all ", e)
            return None

    # METODO GET BY ID (OBTENER ID)
    def get_by_id(id):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""SELECT * FROM types
                        WHERE id = %s;""",(id,))
            type_found = cur.fetchone()
            cur.close()
            conn.close()
            return type_found

        except Exception as e:
            print( "Error get_by_id: ", e)
            return None
        

    # METODO CREAR
    def create(name_type, description):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO types(name, description)
                        VALUES (%s,%s) RETURNING id;
                        """, (name_type, description))
            new_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            return new_id
        except Exception as e:
            print("Error: ", e)
            return None
    
    # METODO ACTUALIZAR
    def update(name_type,id):
        try:

            conn = get_db()
            cur = conn.cursor()
            cur.execute("""UPDATE types SET "name"=%s 
                        WHERE id=%s;
                        """,(name_type, id))
            conn.commit()
            cur.close()
            conn.close()

        except Exception as e:
            print("Error update: ", e)
            return None

    # METODO DELETE
    def delete(id):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""UPDATE types SET deleted_at = now()
                        where id = %s;
                        """,(id,))
            conn.commit()
            cur.close()
            conn.close()
            return True
        except Exception as e:
            print("Error: ", e)
            return None

type_service = Type_service