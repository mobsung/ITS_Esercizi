'''

Generazione link interni

    Usare url_for per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).

'''

from flask import Flask, url_for
# flask run ---> per avviare l'app

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return f"<h3>url: {url_for('show_userprofile', username='Stefano Real')}"\
           f"<h3>url: {url_for('show_userprofile', username='Lorenzo')}"\
           f"<h3>url: {url_for('show_userprofile', username='Marcel')}"
           

@app.route('/user/<string:username>')
def show_userprofile(username:str) -> str:
    return f'Profilo di {username}'

# f"<h3>url: {url_for('show_userprofile', username='Stefano Real')}"