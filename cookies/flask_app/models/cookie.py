from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

db= "cookies_schema"

class Cookie:
    def __init__(self, data):
        self.id=data["id"]
        self.cookietype=data["cookietype"]
        self.buyer=data["buyer"]
        self.numb_box=data["numb_box"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def create(cls,data):
        query="INSERT INTO cookies (cookietype, buyer, numb_box) VALUES (%(cookietype)s, %(buyer)s, %(numb_box)s)"
        return connectToMySQL(db).query_db(query,data)
    @classmethod
    def update(cls,data):
        query="UPDATE cookies SET (cookietype=%(cookietype)s, buyer=%(buyer)s, numb_box =%(numb_box)s WHERE id = %(id)s"
        results =connectToMySQL(db).query_db(query, data)
        return results
    @classmethod
    def get_all(cls):
        query="SELECT * FROM cookies"
        results= connectToMySQL(db).query_db(query)
        cookies=[]
        for row in results:
            cookies.append(cls(row))
        return cookies
    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM cookies where id = %(id)s"
        results= connectToMySQL(db).query_db(query,data)
        return cls(results[0])
    @classmethod
    def update(cls,data):
        query="UPDATE cookies SET cookietype=%(cookietype)s,numb_box=%(numb_box)s,buyer=%(buyer)s WHERE id=%(id)s"
        results =connectToMySQL(db).query_db(query, data)
        return results
    @staticmethod
    def validate_cookie(cookie):
        is_valid=True
        if len(cookie['cookietype']) <2:
            is_valid=False
            flash("Cookie Type is required and must be more than 2 characters")
        if len(cookie['numb_box']) <1:
            is_valid=False
            flash("Number of boxes must be a valid number")
        if len(cookie['buyer']) <3:
            is_valid=False
            flash("Buyer name must be more than 3 characters")
        return is_valid