create domain Stringa as varchar (100);

create domain CodiceFiscale as char (16)
        check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

create domain IntGEZ as integer
        check (value >= 0);

create domain RealGEZ as Real
        check (value >= 0);

create type Ruolo as enum
        ('Direttore', 'Progettista', 'Segretario');


create table PosizioneMilitare(
    nome Stringa primary key
);

create table Persona(
    cf CodiceFiscale primary key,
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita date not null,
    maternita IntGEZ,
    is_uomo boolean not null,
    is_donna boolean not null,
    pos_uomo Stringa,
    foreign key (pos_uomo) references PosizioneMilitare(nome),

    check(
        (is_uomo = true)
        =
        (pos_uomo is not null)
    ),

    check(
        (is_donna = true)
        =
        (maternita is not null)
    ),

    check(
        is_uomo = true or is_donna = true
    )
);

create table Studente(
    persona CodiceFiscale primary key,
    foreign key (persona) references Persona(cf),
    matricola IntGEZ not null,
    unique(matricola)
);

create table Impiegato(
    persona CodiceFiscale primary key,
    foreign key (persona) references Persona(cf),
    stipendio RealGEZ not null,
    ruolo Ruolo not null
);

create table Progetto(
    id serial primary key,
    nome Stringa not null,
    resp_prog CodiceFiscale not null,
    foreign key (resp_prog) references Impiegato(persona)
);