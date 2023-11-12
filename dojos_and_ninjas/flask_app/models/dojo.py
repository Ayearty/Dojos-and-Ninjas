from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint

class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL('dojosandninjas').query_db(query, data)
        return dojo_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojosandninjas').query_db(query)
        dojos = []
        for b in results:
            dojos.append(cls(b))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls,dojo_id):
        query = """
        SELECT * FROM dojos 
        JOIN ninjas 
        ON dojos.id = ninjas.dojo_id 
        WHERE dojos.id = %(dojo_id)s;
        """
        data={
            "dojo_id" : dojo_id
        }
        results = connectToMySQL('dojosandninjas').query_db(query, data)
        pprint (results)
        dojo = Dojo(results[0])
        for result in results:
            ninja_data = {
                "dojo_id" : result["dojo_id"],
                "id" : result["ninjas.id"],
                "first_name" : result["first_name"],
                "last_name" : result["last_name"],
                "age" : result["age"],
                "created_at" : result["ninjas.created_at"],
                "updated_at" : result["ninjas.updated_at"]
            }
            ninja = Ninja(ninja_data)
            dojo.ninjas.append(ninja)
        return dojo

    @classmethod
    def delete(cls, dojo_id):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        data = {"id": dojo_id}
        return connectToMySQL('dojosandninjas').query_db(query, data)