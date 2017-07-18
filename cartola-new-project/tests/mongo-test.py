
import pandas as pd
from mongo_connection import MongoConnection

## constants

def read_data(filename):
    data = pd.read_csv(filename,error_bad_lines=False)
    return data


#define a string de conexão com instância do mongo
def mongo_connection():
    mongo = MongoConnection()

    atleta = {"id":94105,"apelido":"Devid","clube":"Avaí","posicao":"Atacante","ultima_pontuacao":0,"status":"Nulo","FD":0,"G":0,"CA":0,"FC":0,"FS":0,"DD":0,"GS":0,"PP":0,"SG":0,"CV":0,"FT":0,"A":0,"PE":0,"RB":0,"DP":0,"I":0,"FF":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"R7":0,"R8":0,"R9":0,"R10":0,"R11":0,"R12":None,"P1":1,"P2":1,"P3":1,"P4":1,"P5":1,"P6":1,"P7":1,"P8":1,"P9":1,"P10":1,"P11":1,"P12":None}
    id = mongo.insert_atleta(atleta)

    return id


# MAIN ROUTINE
def main():
    x = mongo_connection()
    #mongo = MongoConnection()

    #data = read_data('../../atletas.csv')
    #json_data = data[0:5].to_json(orient='records')

    #r = mongo.insert_atletas(json_data)


    print(r)

if __name__ == "__main__":
    main()