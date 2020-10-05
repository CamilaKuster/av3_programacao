from config import *
from modelo import Cliente

@app.route("/")
def inicio():
    return 'Sistema de cadastro de clientes. '+\
        '<a href="/listar_clientes">Cheque aqui os listados</a>'

@app.route("/listar_clientes")
def listar_clientes():
   
    clientes = db.session.query(Cliente).all()
 
    clientes_em_json = [ x.json() for x in clientes ]
 
    resposta = jsonify(clientes_em_json)
 
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 


@app.route("/incluir_cliente", methods=['post'])
def incluir_cliente():

    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    dados = request.get_json() 

    try: 
      nova = Cliente(**dados)
      db.session.add(nova) 
      db.session.commit() 
      
    except Exception as e: 
      
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


app.run(debug=True)