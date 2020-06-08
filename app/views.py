import datetime
import json

import requests
from flask import render_template, redirect, request

from app import app

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []

infoLogin = {}
with open("login.txt") as archivo:
    for line in archivo:
       (key, val) = line.split()
       infoLogin[key] = val
print(infoLogin)

infoMiembros = {}
with open("miembrosEntidad.txt") as archivo:
    for line in archivo:
       (key, val) = line.split()
       infoMiembros[key] = val
print(infoMiembros)

def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='Sistema de Transparencia '
                                 'Presupuestal',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    author = request.form["author"]
    monto = request.form["monto"]
    contrasena = request.form["contrasena"]

    # Verificación de usuario y contraseña en diccionario
    if author not in infoLogin or infoLogin[author] != contrasena:
        return redirect('/')

    #Traducción a entidad
    author = infoMiembros[author]

    post_object = {
        'author': author,
        'content': post_content,
        'monto': monto,
        'contrasena': contrasena,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')

@app.route('/solicitar_verificacion', methods=['POST'])
def solicitar_verificacion():

    entidad = request.form["entidades"]

    post_object = {
        'entidad': entidad,
    }

    new_tx_address = "{}/solicitar_verificaciona".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})
    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
