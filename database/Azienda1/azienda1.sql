create domain Stringa as varchar;

create domain RealGEZ as integer
    check (value >= 0);

create type Denaro as(
    valore RealGEZ,
    valuta char(3)
);

create table Impiegato(
    id Integer primary key,
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    stipendio Denaro not null,
    dipartimento Integer not null
    foreign key (dipartimento) references Dipartimento(id)
);

create table Dipartimento(
    id Integer primary key,
    nome Stringa not null,
    telefono Stringa not null,
    dirige Integer unique not null,
    foreign key (dirige) references Impiegato(id)
);

create table afferisce(
    id Integer primary key,
    data_afferenza date not null,
    impiegato Integer not null,
    dipartimento Integer not null,
    foreign key (impiegato) references Impiegato(id),
    foreign key (dipartimento) references Dipartimento(id)
);

create table Progetto(
    id Integer primary key,
    nome Stringa not null,
    budjet Denaro not null
);

create table Partecipa(
    impiegato Integer not null,
    progetto Integer not null,
    primary key (impiegato, progetto),
    foreign key (impiegato) references Impiegato(id),
    foreign key (progetto) references Progetto(id)
);