from app import app
from flask import jsonify, url_for, redirect
from ..views import contatos, helper

@app.route('/v1', methods=['GET'])
@helper.token_required
def root(current_contato):
    return jsonify({'message': f'Hello {current_contato.nome}'})


@app.route('/v1/authenticate', methods=['POST'])
def authenticate():
    return helper.auth()


@app.route('/v1/contatos', methods=['GET'])
def get_contatos():
    return contatos.get_contatos()


@app.route('/v1/contatos/<id>', methods=['GET'])
def get_contato(id):
    return contatos.get_contato(id)


@app.route('/v1/contatos', methods=['POST'])
def post_contatos():
    return contatos.post_contato()


@app.route('/v1/contatos/<id>', methods=['DELETE'])
def delete_contatos(id):
    return contatos.delete_contato(id)


@app.route('/v1/contatos/<id>', methods=['PUT'])
def update_contatos(id):
    return contatos.update_contato(id)

@app.route('/v1/auth', methods=['POST'])
def auth():
    pass
