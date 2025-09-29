-- 1. Quanti sono gli strutturati di ogni fascia?

select posizione, count(posizione) from Persona
group by posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count(*) as numero from Persona
where stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*) as numero from Progetto
where budget > 50000
	and fine < CURRENT_DATE;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?

select avg(oredurata) as media, min(oredurata) as minimo, max(oredurata) as massimo
from Progetto p, AttivitaProgetto ap
where nome = 'Pegasus'
	and p.id = ap.progetto;

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?

select pr.id as id_persona, avg(oredurata) as media, min(oredurata) as minimo, max(oredurata) as massimo
from Progetto p, AttivitaProgetto ap, Persona pr
where p.nome = 'Pegasus'
	and p.id = ap.progetto
	and ap.persona = pr.id
group by pr.id


-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select p.id as id_persona, nome, cognome, sum(oredurata) as ore_didattica
from persona p, AttivitaNonProgettuale anp
where p.id = anp.persona
	and tipo = 'Didattica'
group by p.id;


-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(stipendio) as media, min(stipendio) as minimo, max(stipendio) as massimo
from persona p
where posizione = 'Ricercatore';


-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?

select posizione, avg(stipendio) as media, min(stipendio) as minimo, max(stipendio) as massimo
from persona p
group by posizione;


-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?


select pr.id as id_progetto, pr.nome, sum(oredurata) as totale_ore
from persona p, AttivitaProgetto ap, progetto pr
where p.id = ap.persona
	and ap.progetto = pr.id
	and p.nome = 'Ginevra'
	and p.cognome = 'Riva'
group by pr.id
;


-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select pr.id, pr.nome
from persona p, AttivitaProgetto ap, progetto pr
where p.id = ap.persona
	and ap.progetto = pr.id
group by pr.id, pr.nome
having count(distinct p.id) > 2
;
