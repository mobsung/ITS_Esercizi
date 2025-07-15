create domain Stringa as varchar;

create domain IntGZ as Integer
    check ( value > 0);

create domain IntGEZ as Integer
    check ( value >= 0);

create domain IntG1900 as Integer
    check  ( value > 1900);

create table Nazione (
    id Integer primary key,
    nome Stringa not null
);

create table Citta (
    id Integer primary key,
    nome Stringa not null,
    abitanti IntGEZ not null,
    nazione Integer not null,
    foreign key (nazione) references Nazione(id)
);

create table Aeroporto (
    id Integer primary key,
    codice Stringa not null,
    nome Stringa not null,
    citta Integer not null,
    foreign key (citta) references Citta(id)
);

create table CompagniaAerea (
    id Integer primary key,
    nome Stringa not null,
    findazione IntG1900 not null,
    citta Integer not null,
    foreign key (citta) references Citta(id)
);

create table Volo (
    id Integer primary key,
    codice Stringa not null,
    durata_in_minuti IntGZ not null,
    compagnia_aerea Integer not null,
    foreign key (compagnia_aerea) references CompagniaAerea(id),
    aeroporto_arrivo Integer not null,
    foreign key (aeroporto_arrivo) references Aeroporto(id),
    aeroporto_partenza Integer not null,
    foreign key (aeroporto_partenza) references Aeroporto(id)
);