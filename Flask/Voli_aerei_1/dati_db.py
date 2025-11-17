DB = {
    'Nazione': {
        1: {'id': 1, 'nome': 'Italia'},
        2: {'id': 2, 'nome': 'Francia'},
        3: {'id': 3, 'nome': 'Spagna'},
        4: {'id': 4, 'nome': 'Germania'},
        5: {'id': 5, 'nome': 'Svizzera'}
    },

    'Citta': {
        1: {'id': 1, 'n_abitanti': 60000, 'nome': 'Pomezia', 'nazione': 1},
        2: {'id': 2, 'n_abitanti': 2873000, 'nome': 'Roma', 'nazione': 1},
        3: {'id': 3, 'n_abitanti': 2148000, 'nome': 'Parigi', 'nazione': 2},
        4: {'id': 4, 'n_abitanti': 3266000, 'nome': 'Madrid', 'nazione': 3},
        5: {'id': 5, 'n_abitanti': 1841000, 'nome': 'Monaco di Baviera', 'nazione': 4},
        6: {'id': 6, 'n_abitanti': 380000, 'nome': 'Zurigo', 'nazione': 5},
        7: {'id': 7, 'n_abitanti': 650000, 'nome': 'Barcellona', 'nazione': 3}
    },

    'Aereoporto': {
        1: {'id': 1, 'nome': 'Roma Fiumicino', 'codice': 'FCO', 'citta': 2},
        2: {'id': 2, 'nome': 'Roma Ciampino', 'codice': 'CIA', 'citta': 2},
        3: {'id': 3, 'nome': 'Pomezia Aeroporto', 'codice': 'POM', 'citta': 1},
        4: {'id': 4, 'nome': 'Charles de Gaulle', 'codice': 'CDG', 'citta': 3},
        5: {'id': 5, 'nome': 'Orly', 'codice': 'ORY', 'citta': 3},
        6: {'id': 6, 'nome': 'Madrid-Barajas', 'codice': 'MAD', 'citta': 4},
        7: {'id': 7, 'nome': 'Barcellona El Prat', 'codice': 'BCN', 'citta': 7},
        8: {'id': 8, 'nome': 'Zurigo Kloten', 'codice': 'ZRH', 'citta': 6}
    },

    'CompagniaAerea': {
        1: {'id': 1, 'fondazione': 1946, 'nome': 'Alitalia', 'citta': 2},
        2: {'id': 2, 'fondazione': 1984, 'nome': 'Air Pomezia', 'citta': 1},
        3: {'id': 3, 'fondazione': 1933, 'nome': 'Air France', 'citta': 3},
        4: {'id': 4, 'fondazione': 1927, 'nome': 'Iberia', 'citta': 4},
        5: {'id': 5, 'fondazione': 1953, 'nome': 'Lufthansa', 'citta': 5},
        6: {'id': 6, 'fondazione': 2002, 'nome': 'Swiss Air', 'citta': 6}
    },

    'Volo': {
        1: {
            'id': 1, 'durata_in_minuti': 60, 'codice': 'AZ100',
            'compagniaAerea': 1, 'aeroporto_partenza': 1, 'aeroporto_arrivo': 2
        },
        2: {
            'id': 2, 'durata_in_minuti': 90, 'codice': 'AZ200',
            'compagniaAerea': 1, 'aeroporto_partenza': 1, 'aeroporto_arrivo': 4
        },
        3: {
            'id': 3, 'durata_in_minuti': 130, 'codice': 'AF300',
            'compagniaAerea': 3, 'aeroporto_partenza': 4, 'aeroporto_arrivo': 1
        },
        4: {
            'id': 4, 'durata_in_minuti': 110, 'codice': 'IB400',
            'compagniaAerea': 4, 'aeroporto_partenza': 6, 'aeroporto_arrivo': 7
        },
        5: {
            'id': 5, 'durata_in_minuti': 55, 'codice': 'AP500',
            'compagniaAerea': 2, 'aeroporto_partenza': 3, 'aeroporto_arrivo': 1
        },
        6: {
            'id': 6, 'durata_in_minuti': 140, 'codice': 'LH600',
            'compagniaAerea': 5, 'aeroporto_partenza': 8, 'aeroporto_arrivo': 4
        },
        7: {
            'id': 7, 'durata_in_minuti': 100, 'codice': 'SW700',
            'compagniaAerea': 6, 'aeroporto_partenza': 8, 'aeroporto_arrivo': 1
        },
        8: {
            'id': 8, 'durata_in_minuti': 75, 'codice': 'AF800',
            'compagniaAerea': 3, 'aeroporto_partenza': 5, 'aeroporto_arrivo': 7
        },
        9: {
            'id': 9, 'durata_in_minuti': 150, 'codice': 'IB900',
            'compagniaAerea': 4, 'aeroporto_partenza': 6, 'aeroporto_arrivo': 8
        },
        10: {
            'id': 10, 'durata_in_minuti': 35, 'codice': 'AP1000',
            'compagniaAerea': 2, 'aeroporto_partenza': 3, 'aeroporto_arrivo': 2
        }
    }
}

