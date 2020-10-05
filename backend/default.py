from config import *
from modelo import Cliente
#importado tudo de config e importando a classe cliente

@app.route("/")
#quando possui somente a barra é normalmente o index ou o home (a pagina inicial do site)
def inicio():
    return 'Sistema de cadastro de clientes. '+\
        '<a href="/listar_clientes">Operação listar</a>'

@app.route("/listar_clientes")
def listar_clientes():
    clientes = db.session.query(Cliente).all()
    clientes_em_json = [ x.json() for x in clientes ]
    resposta = jsonify(clientes_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

# teste da rota: curl -d '{"nome":"James Kirk", "telefone":"92212-1212", "email":"jakirk@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_pessoa
@app.route("/incluir_cliente", methods=['post'])
def incluir_cliente():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = Cliente(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

app.run(debug=True)

