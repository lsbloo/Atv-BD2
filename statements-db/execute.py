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

class Product(object):
    def __init__(self,nome,codigo,price,descricao,quantidade):
        self.nome=nome
        self.codigo=codigo
        self.price=price
        self.descricao=descricao
        self.quantidade=quantidade

class Categorie(object):
    def __init__(self,tipo,descricao,product):
        self.tipo=tipo
        self.descricao=descricao
        self.product=product

print(database_test.createConnector())
database_test.create_tables()
adress_osvaldo = Address('quiteria reis','1291212','CENTRO','20','pedra','pernambuco')
#database_test.insert_adress(adress_osvaldo)
product_01 = Product('Arroz','123','5.00','Arroz Integral 001','320')
product_02 = Product('','3','100','',0)
#database_test.insert_product(product_01)
database_test.insert_product(product_02)

osvaldo = Client('osvaldo','1821928','osvaldo.airon@dcx.ufpb.br',1)
#database_test.insert_client(osvaldo)
categorie1 = Categorie('Alimento','Alimentos Pereciveis',1)
categorie2 = Categorie('Alimento','Alimentos Pereciveis',2)

#database_test.insert_categories(categorie1)
#database_test.insert_categories(categorie2)

print("Projeção: " , database_test.get_projection_join(None))