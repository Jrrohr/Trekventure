from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Game:
    def __init__( self , data ):
        self.id = data['id']
        self.shirt = data['shirt']
        self.page_number = data['page_number']
        self.name = data['name']
        self.explore = data['explore']
        self.location = data['location']
        self.encounter = data['encounter']
        self.friendly = data['friendly']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO games ( shirt, page_number, name, explore, location, encounter, friendly, user_id) VALUES (%(shirt)s, %(page_number)s, %(name)s, %(explore)s, %(location)s, %(encounter)s, %(friendly)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def getbyid(cls, id):
        data = {
            "id" : id
        }
        query = "SELECT * FROM games WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results and len(results) > 0:
            one_game = cls(results[0])
            return one_game
        else:
            return False

    @classmethod
    def updategame(cls, data):
        query = "UPDATE games SET shirt = %(shirt)s, page_number = %(page_number)s, name = %(name)s, explore = %(explore)s, location = %(location)s, encounter = %(encounter)s, friendly = %(friendly)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls, id):
        data = {
            "id" : id
        }
        query = "SELECT * FROM games JOIN users ON users.id = games.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        games = []
        if results:
            for row in results:
                game = cls(row)
                games.append(game)
        return games