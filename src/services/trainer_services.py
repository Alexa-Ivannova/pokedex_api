from src.db import get_db

# DEPENDENCIAS
from datetime import datetime  #DEPENDENCIA PARA FECHA


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

    # METODO GET_BY_ID:
    def get_by_id(self, id):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                        SELECT * FROM trainers
                        WHERE id = %s;
                        """,(id,))
            
            type_found = cur.fetchone()
            cur.close
            conn.close
            return type_found
        
        except Exception as e:
            print("Error traer entrenador por id ", e)
            return None


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
    def update_trainer(self, data):
        try: 

            id = data.get("id")
            name = data.get("name")
            region = data.get("region")
            deleted_at = data.get("deleted_at")

            conn = get_db()
            cur = conn.cursor()

            if name:
                cur.execute("""
                            UPDATE trainers SET "name"= %s
                            where id =%s;
                            """,(name,id))
            
            if region:
                cur.execute("""
                            UPDATE trainers SET region= %s
                            where id = %s
                            ;
                            """,(region,id))
                
            if deleted_at:
                cur.execute("""
                            UPDATE trainers SET deleted_at = %s
                            where id = %s;
                            """, (deleted_at, id))
            
            conn.commit() 
            cur.close()
            conn.close()
            
            id_return = self.get_by_id(id)

            return id_return
        
        except Exception as e:
            print("Error update trainer: ", e)
            return None
    
    
    # METODO DELETE 
    def delete_trainer(self, id):
        try:

            data = {
                "id": id,
                "deleted_at": datetime.now()
            }

            self.update_trainer(data)
            
        except Exception as e:
            print("Error delete trainer: ", e)
            return None
        
trainer_service = Trainer_service()