from src.db import get_db


class Type_service: 

    # METODO GET (OBTENER TODOS)

    # METODO GET BY ID (OBTENER ID)

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