import re
from flask.templating import render_template
from sqlalchemy.sql.elements import Null

from werkzeug.utils import secure_filename
# Importa todas as configurações feitas
from config import *
# Importa as tabelas do modelo
from modelo import Comentario, Roupa

@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_comentarios")
def listar_pessoas():
    # Recupera os dados do backend
    comentarios = db.session.query(Comentario).all()
    # Cria a lista para salvar os dados
    retorno = []
    # Navega a lista de comentários
    for i in comentarios:
        # Adiciona a versão json dos comentários na lista de retorno
        retorno.append(i.json())

    # Transforma a lista em um json
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    # Retorna para o frontend
    return resposta

@app.route("/incluir_comentario", methods=['post'])
def incluir_cidadao():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    # Variavel que identifica se tem erros
    semErro = True
    try: # tentar executar a operação
        # Caso a operação não tenha erros, faz o registro
        if semErro == True:
            nova = Comentario(**dados) # criar a nova pessoa
            db.session.add(nova) # adicionar no BD
            db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

@app.route("/deletar_comentario", methods=['post'])
def deletar_comentario():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    # Variavel que identifica se tem erros
    deletara = Comentario.query.filter_by(Id=dados['Id']).first()

    db.session.delete(deletara)
    db.session.commit() # Grava os dados no banco de dados
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

@app.route("/listar_roupas")
def listar_roupas():
    # Recupera os dados do backend
    roupas = db.session.query(Roupa).all()
    # Cria a lista para salvar os dados
    retorno = []
    # Navega a lista de comentários
    for i in roupas:
        # Adiciona a versão json dos comentários na lista de retorno
        retorno.append(i.json())

    # Transforma a lista em um json
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    # Retorna para o frontend
    return resposta

app.run(debug=True)