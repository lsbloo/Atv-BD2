from variables import DATABASE_NAME,DATABASE_HOST_CONNECT,DATABASE_USER,DATABASE_PASSWORD,DATABASE_PORT
from database import DataBase


database_test = DataBase(DATABASE_NAME,DATABASE_HOST_CONNECT,DATABASE_USER,DATABASE_PASSWORD,DATABASE_PORT)
class Client(object):
    def __init__(self,nome,cpf,email,adress_id):
        self.nome=nome
        self.cpf=cpf
        self.email=email
        self.adress_id=adress_id

class Address(object):
    def __init__(self,rua,cep,bairro,numero,cidade,estado):
        self.rua=rua
        self.cep=cep
        self.bairro=bairro
        self.numero=numero
        self.cidade=cidade
        self.estado=estado

print(database_test.createConnector())
database_test.create_tables()
adress_osvaldo = Address('quiteria reis','1291212','CENTRO','20','pedra','pernambuco')
#database_test.insert_adress(adress_osvaldo)

osvaldo = Client('osvaldo','1821928','osvaldo.airon@dcx.ufpb.br',1)
#database_test.insert_client(osvaldo)

