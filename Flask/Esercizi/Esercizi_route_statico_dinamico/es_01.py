'''


Route dinamica per profilo utente

    Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.

    Testare con nomi diversi nell’URL.


'''

from flask import Flask
# flask run ---> per avviare l'app

app = Flask(__name__)

@app.route('/')
def homes() -> str:
    return '<h1> CIAO CIAOCIAO'

@app.route('/user/<string:username>')
def greet(username:str) -> str:
    return f'Benvenuto, {username}'
