'''

    Mini blog

        Definire route /post/<int:id> che restituisca un articolo fittizio.

        Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.

'''

from flask import Flask, url_for
# flask run ---> per avviare l'app

app = Flask(__name__)

utenti: list[str] = ['Stefano', 'Lorenzo', 'Marcel', 'Cristiano']

@app.route('/')
def home() -> str:
    str_out: str = ''
    for utente in utenti:
        str_out += f"<h3>Utente: {utente} -> url: {url_for('show_userprofile', username=f'{utente}')}\n"
    
    return str_out

        

@app.route('/user/<string:username>')
def show_userprofile(username:str) -> str:
    return f'Profilo di {username}'