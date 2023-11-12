from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.dojo_id = db_data['dojo_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save (cls,data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
        VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        """
        return connectToMySQL('dojosandninjas').query_db(query,data)
    
    @classmethod
    def delete(cls, ninja_id):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        return connectToMySQL('dojosandninjas').query_db(query, data)
