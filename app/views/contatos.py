from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.contatos import Contatos, contato_schema, contatos_schema


def get_contatos():
    nome = request.args.get('nome')
    if nome:
        contatos = Contatos.query.filter(Contatos.nome.like(f'%{nome}%')).all()
    else:
        contatos = Contatos.query.all()
    if contatos:
        result = contatos_schema.dump(contatos)
        return jsonify({'message': 'sucesso', 'data': result.data})

    return jsonify({'message': 'nenhum contato encontrado', 'data': {}})


def get_contato(id):
    contato = Contatos.query.get(id)
    if contato:
        result = contato_schema.dump(contato)
        return jsonify({'message': 'sucesso', 'data': result.data}), 201

    return jsonify({'message': "contato nao existe", 'data': {}}), 404


def post_contato():
    username = request.json['username']
    password = request.json['password']
    nome = request.json['nome']
    canal = request.json['canal']
    valor = request.json['valor']
    obs = request.json['obs']

    contato = user_by_username(username)

    if contato:
        result = contato_schema.dump(contato)
        return jsonify({'message': 'user already exists', 'data': {}})

    pass_hash = generate_password_hash(password)
    user = Contatos(username, pass_hash, nome, canal, valor, obs)

    try:
        db.session.add(user)
        db.session.commit()
        result = contato_schema.dump(user)
        return jsonify({'message': 'cadastro feito com sucesso', 'data': result.data}), 201
    except:
        return jsonify({'message': 'error interno no servidor', 'data': {}}), 500


def update_contato(id):
    username = request.json['username']
    password = request.json['password']
    nome = request.json['nome']
    canal = request.json['canal']
    valor = request.json['valor']
    obs = request.json['obs']

    user = Contatos.query.get(id)

    if not user:
        return jsonify({'message': "contato nao existe", 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    if user:
        try:
            user.username = username
            user.password = pass_hash
            user.nome = nome
            user.canal = canal
            user.valor = valor
            user.obs = obs
            db.session.commit()
            result = contato_schema.dump(user)
            return jsonify({'message': 'atualizacao feita com sucesso', 'data': result.data}), 201
        except:
            return jsonify({'message': 'error interno no servidor', 'data':{}}), 500


def delete_contato(id):
    user = Contatos.query.get(id)
    if not user:
        return jsonify({'message': "contato nao existe", 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = contato_schema.dump(user)
            return jsonify({'message': 'exclusao feita com sucesso', 'data': result.data}), 200
        except:
            return jsonify({'message': 'error interno no servidor', 'data': {}}), 500


def user_by_username(username):
    try:
        return Contatos.query.filter(Contatos.username == username).one()
    except:
        return None