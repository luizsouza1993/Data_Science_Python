import collections
from pymongo import MongoClient
import datetime

conn = MongoClient("mongodb+srv://luiz:Pb912010@cluster0.jplkm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl=True,ssl_cert_reqs='CERT_NONE')

db = conn.cadastrodb

collections = db.cadastrodb

post1 = {"Id_produto": "ID:999999999",
         "Produto": "Geladeira",
         "Marca": ["Brastemp","Consul","Electrolux"],
         "Data":datetime.datetime.utcnow()}

collections = db.posts

post_id = collections.insert_one(post1).inserted_id

post2 = {"Id_produto": "ID:88888888",
         "Produto": "Fogão",
         "Marca": ["Brastemp","Consul","Electrolux"],
         "Data":datetime.datetime.utcnow()}

collections= db.posts

post_id = collections.insert_one(post2).inserted_id

for post in collections.find():
    print(post)


