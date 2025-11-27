'''


Route con parametri numerici

    Definire /square/<int:n> che ritorni il quadrato di n.


'''


from flask import Flask
# flask run ---> per avviare l'app

app = Flask(__name__)

@app.route('/')
def homes() -> str:
    return '<h1> CIAO CIAOCIAO'

@app.route('/square/<int:n>')
def greet(n:int) -> str:
    return f'Il quadrato di {n} è {n ** 2}'