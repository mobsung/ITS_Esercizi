-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?

select a.codice, a.nome, count(distinct comp)
from ArrPart ap, Aeroporto a
where ap.partenza = a.codice
	or ap.arrivo = a.codice
group by a.codice
order by a.codice
;

-- 2 ) 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?

select count(v.codice)
from ArrPart ap, Volo v
where partenza = 'HTR'
	and ap.codice  = v.codice
	and ap.comp = v.comp
	and durataminuti >= 100
;


-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?

select nazione, count(distinct aeroporto)
from LuogoAeroporto la, ArrPart ap
where (la.aeroporto = ap.arrivo or la.aeroporto = ap.partenza)
	and ap.comp = 'Apitalia'
group by nazione
order by nazione
;


-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’ ?

select avg(durataMinuti) as media, 
	min(durataMinuti) as minimo,
	max(durataMinuti) as massimo
from Volo v
where v.comp = 'MagicFly'
;

-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti?

select a.codice, a.nome, min(annoFondaz)
from Compagnia c, Aeroporto a, ArrPart ap
where (ap.arrivo = a.codice or ap.partenza = a.codice)
	and ap.comp = c.nome
group by a.codice
;

-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
-- voli?

select la1.nazione, count(distinct la2.nazione)
from LuogoAeroporto la1, LuogoAeroporto la2, ArrPart ap
where la1.aeroporto = ap.arrivo
	and la2.aeroporto = ap.partenza
	and la1.nazione <> la2.nazione
group by la1.nazione
;

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select a.codice, a.nome, avg(v.durataMinuti)
from Aeroporto a, ArrPart ap, Volo v
where ap.partenza = a.codice
	and ap.codice = v.codice
	and ap.comp = v.comp
group by a.codice
;


-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?

select c.nome, sum(v.durataMinuti)
from Compagnia c, Volo v
where v.comp = c.nome
	and c.annoFondaz >= 1950
group by c.nome
;

-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.codice, a.nome
from Aeroporto a, ArrPart ap
where (ap.arrivo = a.codice or ap.partenza = a.codice)
group by a.codice
having count(distinct ap.comp) = 2
order by a.codice
;

-- 10. Quali sono le città con almeno due aeroporti?

select citta
from LuogoAeroporto la
group by la.citta
having count(*) > 1
;

-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
-- ore?

select v.comp
from Volo v
group by v.comp
having avg(v.durataMinuti) > 360
order by v.comp
;

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
-- minuti?

select v.comp
from Volo v
group by v.comp
having min(v.durataMinuti) > 100
order by v.comp
;

-- 13. Qual è il nome delle compagnie che non ha alcun -- volo


select distinct(c.nome)
from Compagnia c
where c.nome not in (select comp from Volo)
;