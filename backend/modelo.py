from config import *

class Cliente(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    cpf = db.Column(db.String(20))
    rg = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    endereco = db.Column(db.String(20))


    def __str__(self):
        return str(self.id)+") "+ self.username + ", " + self.password + ", " + self.name + ", " + self.email + ", " + self.cpf + ", " + self.rg + ", " + self.celular + ", " + self.endereco 
    
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
            "endereco": self.endereco
        }


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)


    db.create_all()


    clienteum = Cliente(username = "Camz", password = "123", name = "Camila", email = "camilaparecida.k@gmail.com", cpf = "123456", rg = "7890", celular = "96439183", endereco = "Rua Acacio Bernardes")
    clientedois = Cliente(username = "Carol", password = "456", name = "Carolina", email = "carol.k@gmail.com", cpf = "78901", rg = "24356", celular = "9631393", endereco = "Rua Dr Pedro Zimmermman")
    clientetres = Cliente(username = "Le", password = "789", name = "Leticia", email = "leticia.k@gmail.com", cpf = "34566", rg = "1526", celular = "943526", endereco = "Rua Marilene Figueiredo Loch")
    

    db.session.add(clienteum)
    db.session.add(clientedois)
    db.session.add(clientetres)
    db.session.commit()
    

    print(clienteum)
    print(clientedois)
    print(clientetres)

    
    print(clienteum.json())
    print(clientedois.json())
    print(clientetres.json())