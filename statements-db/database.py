import psycopg2

commands_create_tables = [
    
    ("CREATE TABLE IF NOT EXISTS address (id SERIAL PRIMARY KEY, rua varchar(255) , cep varchar(255), bairro varchar(255), numero varchar(255), cidade varchar(255), estado varchar(255));"),
    ("CREATE TABLE IF NOT EXISTS client (id SERIAL PRIMARY KEY, nome varchar(255), cpf varchar(255), email varchar(255), adress_id INTEGER, FOREIGN KEY (id) REFERENCES address(id));"),
    ("CREATE TABLE IF NOT EXISTS product (id SERIAL PRIMARY KEY, nome varchar(255), codigo varchar(255), price varchar(255), descricao varchar(255), quantidade INTEGER );"),
    ("CREATE TABLE IF NOT EXISTS pedido (id SERIAL PRIMARY KEY, codigo_pedido varchar(255), products_id INTEGER, FOREIGN KEY (id) REFERENCES product(id));"),
    ("CREATE TABLE IF NOT EXISTS categoria (id SERIAL PRIMARY KEY, tipo varchar(255) , descricao varchar(255), product INTEGER,  UNIQUE(product), FOREIGN KEY (product) REFERENCES product(id));")
]
commands_getter_tables = [
    (
        
    )
]

class DataBase(object):

    def __init__(self,database_name,database_host_connect,database_user,database_password,database_port):
        self.database_name=database_name
        self.database_host_connect=database_host_connect
        self.database_user=database_user
        self.database_password=database_password
        self.database_port=database_port

    def createConnector(self):
        self.connector = psycopg2.connect(host=self.database_host_connect,dbname=self.database_name,
        user=self.database_user,password=self.database_password,port=self.database_port)
        self.connector.autocommit = True
        if self.connector != None:
            return self.connector
        return None

    def create_tables(self):
        cursor = self.connector.cursor()
        for i in range(len(commands_create_tables)):
            res = cursor.execute(commands_create_tables[i])
        cursor.close()
        return 'Tables created'

    def insert_adress(self,adress):
        cursor = self.connector.cursor()
        data=(adress.rua,adress.cep,adress.bairro,adress.numero,adress.cidade,adress.estado)
        sql=("INSERT INTO address (rua,cep,bairro,numero,cidade,estado) VALUES ('%s','%s','%s','%s','%s','%s')"
        %(adress.rua,adress.cep,adress.bairro,adress.numero,adress.cidade,adress.estado))
        cursor.execute(sql)
        cursor.close()

    def insert_client(self,client):
        cursor = self.connector.cursor()
        data=(client)
        sql=("INSERT INTO client (nome,cpf,email,adress_id) VALUES ('%s','%s','%s','%s')"%(client.nome,client.cpf,client.email,client.adress_id))
        cursor.execute(sql)
        cursor.close()
    def insert_product(self,product):
        cursor = self.connector.cursor()
        data=(product)
        sql =("INSERT INTO product (nome,codigo,price,descricao,quantidade) values ('%s','%s','%s','%s','%s')"%(product.nome,product.codigo,product.price,product.descricao,product.quantidade))
        cursor.execute(sql)
        cursor.close()
    
    def insert_categories(self,categorie):
        cursor = self.connector.cursor()
        data=(categorie)
        sql = ("INSERT INTO categoria (tipo,descricao,product) values ('%s', '%s','%s')"%(categorie.tipo,categorie.descricao,categorie.product))
        cursor.execute(sql)
        cursor.close()

    def get_projection_join(self,id_products):
        cursor = self.connector.cursor()
        sql = ("SELECT nome,price from product INNER JOIN categoria ON categoria.product=product.id")
        cursor.execute(sql)
        return cursor.fetchall()
    
        