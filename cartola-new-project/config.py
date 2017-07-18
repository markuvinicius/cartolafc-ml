from util import Struct as Section

mongodb = Section("MongoDB Configurations")
mongodb.host = 'mongodb://localhost:27017/'
mongodb.database = 'cartola_db'

mongodb.collections = Section("Collections for Mongodb")
mongodb.collections.atletas = 'atletas'
mongodb.collections.clubes = 'clubes'
mongodb.collections.tabela = 'tabela'

