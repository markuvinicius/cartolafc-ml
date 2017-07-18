from pymongo import MongoClient
import config as CONFIG

class MongoConnection(object):

    db = None
    atletas = None
    clubes = None

    def __init__(self, *args):
        self.__header__ = str(args[0]) if args else None

        #instancia conexão com mongodb
        client = MongoClient(CONFIG.mongodb.host)
        self.db = client[CONFIG.mongodb.database]

        #inicia as collections atletas e clubes
        self.atletas = self.db[CONFIG.mongodb.collections.atletas]
        self.clubes = self.db[CONFIG.mongodb.collections.clubes]


    def __repr__(self):
        if self.__header__ is None:
             return super(MongoConnection, self).__repr__()
        return self.__header__


    def insert_atleta(self,data):
        atleta_id = self.atletas.insert_one(data).inserted_id
        return atleta_id

    def insert_atletas(self,data):
        result = self.atletas.insert_many(data)
        return result.inserted_ids