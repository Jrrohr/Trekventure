from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE, bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register( cls , data ):
        query = "INSERT INTO users ( username, email, password) VALUES (%(username)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def find_by_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results and len(results) > 0:
            one_user = cls(results[0])
            return one_user
        else:
            return False

    @classmethod
    def find_by_id(cls, id):
        data = {
            "id" : id
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results and len(results) > 0:
            one_user = cls(results[0])
            return one_user
        else:
            return False

    @classmethod
    def validate_login(cls, data):
        one_user = cls.find_by_username(data)
        if len(data['username']) < 1 or len(data['password']) < 1:
            flash("Fields cannot be blank", 'login')
            return False
        if not one_user:
            flash("Invalid login", 'login')
            return False
        elif not bcrypt.check_password_hash(one_user.password, data['password']):
            flash("Invalid login", 'login')
            return False
        return one_user

    @staticmethod
    def validate(user):
        is_valid = True # we assume this is true
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, user)
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters.", 'register')
            is_valid = False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'register')
            is_valid = False
        elif len(results) >= 1:
            flash("This email is already in the system", 'register')
            is_valid = False

        if user['password'] != user['confirm_password']:
            flash("Passwords don't match", 'register')
            is_valid = False

        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", 'register')
            is_valid = False
        return is_valid
