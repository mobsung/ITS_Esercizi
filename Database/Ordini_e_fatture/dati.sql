-- Dati per la tabella Nazione (3 esempi)
INSERT INTO Nazione (nome) VALUES
('Italia'),
('Francia'),
('Germania');

-- Dati per la tabella Regione (6 esempi)
INSERT INTO Regione (nome, nazione) VALUES
('Lazio', 'Italia'),
('Lombardia', 'Italia'),
('Campania', 'Italia'),
('Ile-de-France', 'Francia'),
('Baviera', 'Germania'),
('Renania Settentrionale-Vestfalia', 'Germania');

-- Dati per la tabella Citta (9 esempi)
INSERT INTO Citta (nome, regione, nazione) VALUES
('Roma', 'Lazio', 'Italia'),
('Milano', 'Lombardia', 'Italia'),
('Napoli', 'Campania', 'Italia'),
('Parigi', 'Ile-de-France', 'Francia'),
('Monaco di Baviera', 'Baviera', 'Germania'),
('Colonia', 'Renania Settentrionale-Vestfalia', 'Germania');

-- Dati per la tabella Direttore (5 esempi)
INSERT INTO Direttore (cf, nome, cognome, data_nascita, anni_servizio, citta, regione, nazione) VALUES
('RSSMRA80A01H501K', 'Mario', 'Rossi', '1980-01-15', 10, 'Roma', 'Lazio', 'Italia'),
('BNCLCU75C20F839J', 'Luca', 'Bianchi', '1975-03-20', 15, 'Milano', 'Lombardia', 'Italia'),
('VRDLDA82E05G273P', 'Laura', 'Verdi', '1982-05-05', 8, 'Napoli', 'Campania', 'Italia'),
('GRGPLA78B10A123Z', 'Paolo', 'Grigi', '1978-02-10', 12, 'Parigi', 'Ile-de-France', 'Francia'),
('BNCFRN85S25L400M', 'Francesca', 'Bruni', '1985-09-25', 5, 'Colonia', 'Renania Settentrionale-Vestfalia', 'Germania');

-- Dati per la tabella Dipartimento (5 esempi)
INSERT INTO Dipartimento (nome, indirizzo, direttore) VALUES
('Amministrazione', ROW('Via del Corso', '10', '00186')::Indirizzo, 'RSSMRA80A01H501K'),
('Produzione', ROW('Via Montenapoleone', '25', '20121')::Indirizzo, 'BNCLCU75C20F839J'),
('Ricerca e Sviluppo', ROW('Corso Umberto I', '50', '80138')::Indirizzo, 'VRDLDA82E05G273P'),
('Marketing', ROW('Rue de Rivoli', '100', '75001')::Indirizzo, 'GRGPLA78B10A123Z'),
('Logistica', ROW('Hohenzollernring', '30', '50672')::Indirizzo, 'BNCFRN85S25L400M');

-- Dati per la tabella Fornitore (5 esempi)
INSERT INTO Fornitore (partitaIVA, ragione_sociale, indirizzo, telefono, email) VALUES
('01234567890', 'Alpha Forniture S.p.A.', ROW('Via Roma', '1', '00100')::Indirizzo, '+39061234567', 'info@alpha.it'),
('09876543210', 'Beta Componenti S.r.l.', ROW('Via Garibaldi', '2', '20100')::Indirizzo, '+39029876543', 'contatti@beta.it'),
('11223344556', 'Gamma Servizi S.a.s.', ROW('Piazza Duomo', '3', '80100')::Indirizzo, '+39081112233', 'commerciale@gamma.it'),
('65432109876', 'Delta Tech GmbH', ROW('Hauptstrasse', '15', '10115')::Indirizzo, '+49309876543', 'sales@delta.de'),
('77889900112', 'Epsilon Solutions Ltd.', ROW('Baker Street', '221B', 'SW1A0AA')::Indirizzo, '+442071234567', 'support@epsilon.co.uk');

-- Dati per la tabella Ordine (15 esempi per arrivare a 30+ totali)
INSERT INTO Ordine (id, data_stipula, imponibile, aliquotaIVA, descrizione, stato, dipartimento, fornitore) VALUES
(1, '2024-01-10', 1500.00, 0.22, 'Acquisto materiale ufficio', 'saldato', 'Amministrazione', '01234567890'),
(2, '2024-01-15', 5000.00, 0.22, 'Componenti elettronici', 'in preparazione', 'Produzione', '09876543210'),
(3, '2024-01-20', 250.00, 0.04, 'Servizio di pulizia', 'da saldare', 'Amministrazione', '11223344556'),
(4, '2024-02-01', 12000.00, 0.19, 'Software di sviluppo', 'inviato', 'Ricerca e Sviluppo', '65432109876'),
(5, '2024-02-05', 750.00, 0.22, 'Campagna pubblicitaria', 'saldato', 'Marketing', '01234567890'),
(6, '2024-02-10', 3000.00, 0.22, 'Nuove attrezzature', 'in preparazione', 'Produzione', '09876543210'),
(7, '2024-02-15', 400.00, 0.10, 'Consulenza IT', 'da saldare', 'Amministrazione', '11223344556'),
(8, '2024-03-01', 8000.00, 0.19, 'Hardware server', 'inviato', 'Ricerca e Sviluppo', '65432109876'),
(9, '2024-03-05', 1000.00, 0.22, 'Materiale promozionale', 'saldato', 'Marketing', '01234567890'),
(10, '2024-03-10', 2000.00, 0.22, 'Materie prime', 'in preparazione', 'Produzione', '09876543210'),
(11, '2024-03-15', 600.00, 0.04, 'Manutenzione impianti', 'da saldare', 'Logistica', '11223344556'),
(12, '2024-04-01', 15000.00, 0.19, 'Licenze software', 'inviato', 'Ricerca e Sviluppo', '65432109876'),
(13, '2024-04-05', 900.00, 0.22, 'Servizi fotografici', 'saldato', 'Marketing', '01234567890'),
(14, '2024-04-10', 4500.00, 0.22, 'Ricambi macchinari', 'in preparazione', 'Produzione', '09876543210'),
(15, '2024-04-15', 300.00, 0.10, 'Corso di formazione', 'da saldare', 'Amministrazione', '77889900112');
