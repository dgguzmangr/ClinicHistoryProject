from pymongo import MongoClient
import json
import certifi

ca = certifi.where()


###################################
# cargar archivo de configuración #
###################################


def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data


######################################
#       Función de conexión          #
######################################

def dbConnection():
    dataConfig = loadConfigFile()
    try:
        # conexión Atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile=ca)
        # Conexión local
        # client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig ['LOCAL_PORT'])
        db = client["BackEnd_ClinicHistory"]
    except ConnectionError:
        print("Error de conexión con la db")
    return db
