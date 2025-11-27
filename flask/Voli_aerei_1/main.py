from flask import Flask, request, jsonify
from dati_db import DB

app = Flask(__name__)


@app.route('/Nazioni', methods=['GET', 'POST'])
def handle_nazioni():
    nazioni = DB['Nazione']
    
    if request.method == 'GET':
        return jsonify(nazioni)
    
    if request.method == 'POST':
        dati = request.get_json()

        if not dati or 'nome' not in dati:
            return {'errore': 'Nome obbligatorio'}, 400

        nuova_nazione = {
                'id': len(nazioni) + 1,
                'nome': dati['nome']
            }
    
        nazioni[len(nazioni) + 1] = nuova_nazione

        return jsonify(nuova_nazione), 201


@app.route('/Citta', methods=['GET', 'POST'])
def handle_citta():
    citta = DB['Citta']

    if request.method == 'GET':
        return jsonify(citta)
    
    if request.method == 'POST':
        dati = request.get_json()

        if not dati or 'n_abitanti' not in dati or 'nome' not in dati or 'nazione' not in dati:
            return {'errore': 'Dati obbligatori'}, 400
    
        if dati.get('nazione') not in DB['Nazione']:
            return {'errore': 'nazione inesistente'}, 400
    
        nuovo_id = len(citta) + 1

        nuova_citta = {
            'id': nuovo_id,
            'n_abitanti': dati['n_abitanti'],
            'nome': dati['nome'],
            'nazione': dati['nazione']
        }

        citta[nuovo_id] = nuova_citta

        return jsonify(nuova_citta)


@app.route('/Aeroporti', methods=['GET', 'POST'])
def handle_aeroporto():
    aeroporti = DB['Aeroporto']

    if request.method == 'GET':
        return jsonify(aeroporti)
    
    if request.method == 'POST':
        dati = request.get_json()

        if not dati or 'nome' not in dati or 'codice' not in dati or 'citta' not in dati:
            return {'errore': 'Dati obbligatori'}, 400
        
        if dati.get('citta') not in DB['Citta']:
            return {'errore': 'citta inesistente'}, 400
        
        nuovo_id = len(aeroporti) + 1
        nuovo_aeroporto = {
            'id': nuovo_id,
            'nome': dati['nome'],
            'codice': dati['codice'],
            'citta': dati['citta']
        }

        aeroporti[nuovo_id] = nuovo_aeroporto

        return jsonify(nuovo_aeroporto)



@app.route('/CompagnieAeree', methods=['GET', 'POST'])
def handle_compagniaAerea():
    compagnieAeree = DB['CompagniaAerea']

    if request.method == 'GET':
        return jsonify(compagnieAeree)
    
    if request.method == 'POST':
        dati = request.get_json()

        if not dati or 'fondazione' not in dati or 'nome' not in dati or 'citta' not in dati:
            return {'errore': 'Dati obbligatori'}, 400

        if dati['citta'] not in DB['Citta']:
            return {'errore': 'citta inesistente'}, 400
        
        nuovo_id = len(compagnieAeree) + 1
        nuova_compagniaAerea = {
            'id': nuovo_id,
            'fondazione': dati['fondazione'],
            'nome': dati['nome'],
            'citta': dati['citta']
        }

        compagnieAeree[nuovo_id] = nuova_compagniaAerea

        return jsonify(nuova_compagniaAerea)





'''
CREATE DOMAIN stringa as varchar;
CREATE DOMAIN intGEZ as integer
        check (value >= 0);
CREATE DOMAIN intGZ as integer
        check (value > 0);
CREATE DOMAIN intG1900 as integer
        check (value > 1900);

CREATE TABLE Nazione(
    id integer primary key,
    nome stringa not null
);

CREATE TABLE Citta(
    id integer primary key,
    n_abitanti intGEZ not null,
    nome stringa not null,
    nazione integer not null,

    foreign key (nazione) references Nazione(id)
);

CREATE TABLE Aereoporto(
    id integer primary key,
    nome stringa not null,
    codice stringa not null,
    citta integer not null,

    foreign key (citta) references Citta(id)
);

CREATE TABLE CompagniaAerea(
    id integer primary key,
    fondazione intG1900 not null,
    nome stringa not null,
    citta integer not null,

    foreign key (citta) references Citta(id)
);

CREATE TABLE Volo(
    id integer primary key,
    durata_in_minuti intGZ not null,
    codice stringa not null,
    compagniaAerea integer not null,
    aeroporto_partenza integer not null,
    aeroporto_arrivo integer not null,

    foreign key (compagniaAerea) references CompagniaAerea(id),
    foreign key (aeroporto_partenza) references Aereoporto(id),
    foreign key (aeroporto_arrivo) references Aereoporto(id)
);
'''