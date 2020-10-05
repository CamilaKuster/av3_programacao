from config import *
#importando tudo de config

class Cliente(db.Model):
    # criando classe cliente e seus atributos
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(300), unique=True, nullable=False) 
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    rg = db.Column(db.Integer, unique=True, nullable=False)
    celular = db.Column(db.Integer, unique=True, nullable=False)
    endereco = db.Column(db.Text, unique=True, nullable=False)

 
    # transformar a classe cliente para ser exibida no formato json
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "email": self.email,
            "cpf": self.cpf,
            "rg": self.rg,
            "celular": self.celular,
            "endereco": self.endereco,     


        }

# teste    .

if __name__=="__main__":
    # serve para não criar infinitamente p1
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    #serve para criar a tabela
    db.create_all()

    # criando uma pessoa
    p1 = Cliente(username='admin',password='123',name='camz',email='camilaa',cpf=123, rg=1233,celular=9643981,endereco="kfekfjgnqaeg")
        
#adicionando p1 e mostrando ela no formato json
    db.session.add(p1)
    db.session.commit()

    print(p1)

    print(p1.json())