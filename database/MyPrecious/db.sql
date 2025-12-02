
BEGIN TRANSACTION;
create domain Stringa AS varchar;

create domain RealGEZ AS real
    CHECK (value >= 0);
COMMIT;

BEGIN TRANSACTION;
create table Nazione (
    nome Stringa primary key
);

create table Regione (
    nome Stringa not null,

    nazione Stringa not null,
    foreign key (nazione)
        references Nazione(nome),

    primary key (nome, nazione)
);

create table Citta (
    nome Stringa not null,

    regione Stringa not null,
    nazione Stringa not null,
    foreign key (regione, nazione)
        references Regione(nome, nazione),
    primary key (nome, regione, nazione)
);

create table Artista (
    id serial primary key,
    nome_arte Stringa not null,
    data_nascita date not null,
    data_morte date,

    check (
        (data_morte is null) or (data_morte > data_nascita)
    )
);

create table Tariffa (
    id serial primary key,
    nome Stringa not null,
    prezzo_base RealGEZ not null
);

create table Biglietto (
    id serial primary key,
    istante_vendita timestamp not null,
    validita date not null,
    check (
        validita >= istante_vendita
    ),
    tariffa integer not null,
    foreign key (tariffa)
        references Tariffa(id)
);

create table Standard (
    biglietto integer primary key,
    foreign key (biglietto)
        references Biglietto(id)
);

create table ExtendedAccess (
    biglietto integer primary key,
    foreign key (biglietto)
        references Biglietto(id)
    -- v.incl. (biglietto) occorre in ext_temp(extended_access)
);


create table Esposizione (
    id serial primary key,
    nome Stringa not null,
    inizio date not null,
    is_temp boolean not null,
    fine date,
    tema Stringa,
    prezzo_accesso RealGEZ,
    check (
        (fine is null) or (fine >= inizio)
        ),
    check (
        (is_temp = true and fine is not null and tema is not null and prezzo_accesso is not null)
            or
        (is_temp = false and fine is null and tema is null and prezzo_accesso is null)
    )
);

create table ext_temp (
    extended_access integer not null,
    foreign key (extended_access)
        references ExtendedAccess(biglietto),
    esposizione_temporanea integer not null,
    foreign key  (esposizione_temporanea)
        references Esposizione,
    primary key (extended_access, esposizione_temporanea)
);

create table Tecnica (
    nome Stringa primary key
);

create table Categoria (
    nome Stringa primary key
);

create table CorrenteArtistica (
    nome Stringa primary key
);

create table Opera (
    id serial primary key,
    nome Stringa not null,
    anno_realizzazione integer not null,
    artista integer,
    foreign key (artista)
        references Artista(id),
    tecnica Stringa,
    foreign key (tecnica)
        references Tecnica(nome),
    categoria Stringa not null,
    foreign key (categoria)
        references Categoria(nome)
    
    -- v.incl. (id) occorre in op_corr(opera)
);

create table op_corr (
    opera integer not null,
    foreign key (opera)
        references Opera(id),
    corrente_artistica Stringa not null,
    foreign key (corrente_artistica)
        references CorrenteArtistica(nome),
    primary key (opera, corrente_artistica)
);

create table espone (
    inizio date not null,
    fine date,
    check (
        (fine is null) or (fine >= inizio)
    ),
    opera integer not null,
    foreign key (opera)
        references Opera(id),
    esposizione integer not null,
    foreign key (esposizione)
        references Esposizione(id),
    primary key (opera, esposizione)
);
COMMIT;