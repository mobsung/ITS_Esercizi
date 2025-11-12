'''

    Mini blog

        Definire route /posts/<int:id> che restituisca un articolo fittizio.

        Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.

'''

from flask import Flask, url_for
# flask run ---> per avviare l'app

app = Flask(__name__)


articoli: dict[int, 'str'] = {
    1: 'penna',
    2: 'matita',
    3: 'gomma',
    4: 'quaderno'
}

@app.route('/')
def home() -> str:
    str_out: str = ''
    for id, articolo in articoli.items():
        str_out += f"<a href='{url_for('show_posts', id=f'{id}')}'>{articolo}<br>"
    
    return str_out

        

@app.route('/posts/<int:id>')
def show_posts(id: int) -> str:
    return f"{articoli[id]} - <a href='/'>Home"