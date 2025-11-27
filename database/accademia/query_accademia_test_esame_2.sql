-- 1. Quali sono le persone con stipendio di al massimo 40000
-- euro [2 punti]

select *
from persona p
where stipendio <= 40000
;

-- 2. Quali sono i ricercatori che lavorano ad almeno un
-- progetto e hanno uno stipendio di al massimo 40000 [2 punti]

select distinct p.id, p.nome, p.cognome
from persona p, attivitaprogetto ap 
where ap.persona = p.id
	and stipendio <= 40000
;


-- 3. Qual è il budget totale dei progetti nel db [2 punti]

select sum(budget)
from progetto p;

-- 4. Qual è il budget totale dei progetti a cui lavora ogni
-- persona. Per ogni persona restituire nome, cognome e
-- budget totale dei progetti nei quali è coinvolto. [3 punti]

select p.nome, p.cognome, sum(pr.budget)
from persona p, progetto pr, attivitaprogetto ap
where ap.persona = p.id
	and ap.progetto = pr.id
group by p.id, p.nome, p.cognome
;

-- 5. Qual è il numero di progetti a cui partecipa ogni
-- professore ordinario. Per ogni professore ordinario,
-- restituire nome, cognome, numero di progetti nei quali è
-- coinvolto [3 punti]

select p.nome, p.cognome, count(pr.id)
from persona p, progetto pr, attivitaprogetto ap
	where ap.persona = p.id
		and ap.progetto = pr.id
		and posizione = 'Professore Ordinario'
group by p.id, p.nome, p.cognome
;

-- 6. Qual è il numero di assenze per malattia di ogni
-- professore associato. Per ogni professore associato,
-- restituire nume, cognome e numero di assenze per
-- malattia [3 punti]

select p.nome, p.cognome, count(a.id)
from persona p, assenza a
where p.id = a.persona
	and a.tipo = 'Malattia'
	and p.posizione = 'Professore Associato'
group by p.id, p.nome, p.cognome
;

-- 7. Qual è il numero totale di ore, per ogni persona, dedicate
-- al progetto con id ‘5’. Per ogni persona che lavora al
-- progetto, restituire nome, cognome e numero di ore totali
-- dedicate ad attività progettuali relative al progetto [4 punti]

select p.nome, p.cognome, count(oredurata)
from persona p, attivitaprogetto ap
where ap.persona = p.id
	and ap.progetto = 5
group by p.id, p.nome, p.cognome
;

-- 8. Qual è il numero medio di ore delle attività progettuali
-- svolte da ogni persona. Per ogni persona, restituire nome,
-- cognome e numero medio di ore delle sue attività
-- progettuali (in qualsivoglia progetto) [3 punti]

select p.nome, p.cognome, avg(oredurata)
from persona p, attivitaprogetto ap
where ap.persona = p.id
group by p.id, p.nome, p.cognome
;

-- 9. Qual è il numero totale di ore, per ogni persona, dedicate
-- alla didattica. Per ogni persona che ha svolto attività
-- didattica, restituire nome, cognome e numero di ore totali
-- dedicate alla didattica [4 punti]

select p.nome, p.cognome, sum(oredurata)
from persona p, attivitanonprogettuale anp
where p.id = anp.persona
	and anp.tipo = 'Didattica'
group by p.id, p.nome, p.cognome
;

-- 10. Quali sono le persone che hanno svolto attività nel WP
-- di id ‘5’ del progetto con id ‘3’. Per ogni persona, restituire
-- il numero totale di ore svolte in attività progettuali per il
-- WP in questione [4 punti]

select ap.persona, sum(oredurata)
from wp, attivitaprogetto ap
where wp.progetto = ap.progetto
and wp.id = ap.wp
	and wp.id = 1
	and ap.progetto = 3
group by ap.persona
;