from bson.objectid import ObjectId
from . import mongo
from flask_login import UserMixin
from datetime import datetime

import sys

sys.setdefaultencoding('utf-8') if hasattr(sys, 'setdefaultencoding') else None

class Post:
    @staticmethod
    def get_all_posts():
        return mongo.db.posts.find()

    @staticmethod
    def get_post(post_id):
        return mongo.db.posts.find_one({'_id': ObjectId(post_id)})

    @staticmethod
    def insert_post(title, content,author,tags):
        return mongo.db.posts.insert_one({'title': title, 'content': content,'when':datetime.now(),'author':author,'tags':tags})
    
    @staticmethod
    def delete_post(post_id):
        try:
            mongo.db.posts.delete_one({'_id': ObjectId(post_id)})
        except Exception as e:
            print(f"Error deleting post: {e}")
            raise

class User(UserMixin):
    def __init__(self, username, email, _id=None):
        self.username = username
        self.email = email
        self.id = str(_id)

    @staticmethod
    def get_user_by_email(email):
        user = mongo.db.users.find_one({'email': email})
        if user:
            return User(username=user['username'], email=user['email'], _id=user['_id'])
        return None

    @staticmethod
    def get_user_by_id(user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return User(username=user['username'], email=user['email'], _id=user['_id'])
        return None

    @staticmethod
    def insert_user(username, email, password):
        return mongo.db.users.insert_one({'username': username, 'email': email, 'password': password})
