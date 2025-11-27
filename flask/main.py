from flask import Flask, url_for

# flask run ---> per avviare l'app

app = Flask(__name__)


@app.route('/')
def homes() -> str:
    return f'<h1>Hello {5+5} World!'


@app.route('/user/<string:username>')
def show_userprofile(username:str) -> str:
    return f'Profilo di {username}'


@app.route('/urls/')
def show_urls() -> str:
    return f"<h3>url: {url_for('show_userprofile', username='Stefano Real')}"
# app.run()

