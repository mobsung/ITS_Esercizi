'''


Parametri multipli

    Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.


'''

from flask import Flask
# flask run ---> per avviare l'app

app = Flask(__name__)

@app.route('/')
def homes() -> str:
    return '<h1> CIAO CIAOCIAO'

@app.route('/sum/<int:a>/<int:b>')
def greet(a:int, b:int) -> str:
    return f'La somma tra {a} e {b} = {a + b}'