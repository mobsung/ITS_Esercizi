create domain Stringa as varchar;

create domain PartitaIVA as char(11)
        check (value ~ '^[0-9]{11}$');

create domain CodiceFiscale as char(16)
        check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

create domain EMail as varchar
        check (value ~ '^[\w\.-]+@[\w\.-]+\.\w{2,}$');

create domain Telefono as varchar(20);

create domain IntGEZ as Integer
        check (value >= 0);

create domain RealGEZ as Real
        check (value >= 0);

create domain RealI01 as Real
        check (value  > 0 and value < 1);

create type Indirizzo as(
        via varchar,
        civico varchar,
        cap char(5)
);

create type Stato as 
    enum ('in preparazione', 'inviato', 'da saldare', 'saldato');

create table Nazione(
    nome Stringa primary key
);

create table Regione(
    nome Stringa not null,
    nazione Stringa not null,
    primary key (nome, nazione),
    foreign key (nazione) references Nazione(nome)
);

create table Citta(
    nome Stringa not null,
    regione Stringa not null,
    nazione Stringa not null,
    primary key (nome, regione, nazione),
    foreign key (regione, nazione) references Regione(nome, nazione)
);

create table Direttore(
    cf CodiceFiscale primary key,
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    anni_servizio IntGEZ not null,
    citta Stringa not null,
    regione Stringa not null,
    nazione Stringa not null,
    foreign key (citta, regione, nazione) references Citta(nome, regione, nazione)
);

create table Dipartimento(
    nome Stringa primary key,
    indirizzo Indirizzo not null,
    direttore CodiceFiscale unique,
    foreign key (direttore) references Direttore(cf)
);

create table Fornitore(
    partitaIVA PartitaIVA primary key,
    ragione_sociale Stringa not null,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email EMail not null
);

create table Ordine(
    id Integer primary key,
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquotaIVA RealI01 not null,
    descrizione Stringa not null,
    stato Stato not null,
    dipartimento Stringa not null,
    fornitore PartitaIVA not null,
    foreign key (dipartimento) references Dipartimento(nome),
    foreign key (fornitore) references Fornitore(partitaIVA)
);