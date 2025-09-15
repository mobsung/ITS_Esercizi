--Quali sono i nomi degli impiegati nati a partire dall'anno 
select nome from Persona, Impiegato
where Persona.cf = Impiegato.persona
order by data_nascita asc;

-- Quali sono i nomi di tutti i progetti?
select nome from Progetto;

-- Quali sono gli stipendi dei direttori?
select stipendio from Impiegato
where ruolo = 'Direttore';

-- Quanti sono i progettisti?
select count (*) from Impiegato
where ruolo = 'Progettista'

-- Quanti sono i responsabili?
select count (*) from Impiegato, Progetto
where Impiegato.persona = Progetto.resp_prog;

-- Qual è lo stipendio medio dei segretari?
select avg(stipendio) from Impiegato
where ruolo = 'Segretario';

-- Qual è l'età della/o studente meno giovane?
-- usare select(date_part('year',age(current_date, <DATA DI NASCITA>))) as eta FROM [...];
select max(date_part('year', age(current_date, data_nascita))) as eta from Persona, Studente
where Persona.cf = Studente.persona;

-- Quanti sono i direttori che hanno assolto agli obblighi militari?
select count(cf) from Persona, Impiegato
where ruolo = 'Direttore'
	and Persona.cf = Impiegato.persona
	and Persona.pos_uomo is not null;

-- Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?
select count(id) from Progetto, Persona
where Persona.cf = Progetto.resp_prog
	and Persona.maternita >= 2;
