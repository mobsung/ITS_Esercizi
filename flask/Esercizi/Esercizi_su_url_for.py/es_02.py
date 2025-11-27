'''


Navigazione dinamica

    Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.


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