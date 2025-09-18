CREATE DOMAIN Stringa AS varchar;
CREATE DOMAIN URL AS varchar(2048);
CREATE DOMAIN IntG1 AS integer
    check (value > 1 );
CREATE DOMAIN IntGEZ AS integer
    check (value >= 0 );
CREATE DOMAIN RealGZ AS Real
    check (value > 0 );
CREATE DOMAIN RealGEZ AS Real
    check (value >= 0 );
CREATE DOMAIN Voto AS integer
    check (value >= 1 and value < = 5)
    
CREATE TYPE condizione AS ENUM
    ('Ottimo', 'Buono', 'Discreto', 'Da sistemare');


create table Categoria(
  nome Stringa primary key,
  super Stringa
);

alter table Categoria 
add constraint fk_categoria_super
foreign key (super) references Categoria(nome);

create table Utente(
    username Stringa primary key,
    registrazione timestamp not null
);

create table PostOggetto(
    id serial primary key,
    descrizione Stringa not null,
    ha_feedback boolean not null,
    voto Voto,
    commento Stringa,
    istante_feedback timestamp,
    utente Stringa not null,
    foreign key (utente)
        references Utente(username),

    check(
            (
                (
                    (ha_feedback = true)
                    =
                    (voto is not null)
                    =
                    (istante_feedback is not null)
                )
            or
                (
                    (
                    (ha_feedback = true)
                    =
                    (voto is not null)
                    =
                    (istante_feedback is not null)
                    )
                    and
                    not(commenoto is not null)
                )
            )
        ),
);

create table MetodoDiPagamento(
    nome Stringa primary key
);

create table PostOggettoUsato(
    pou_isa_po serial primary key,
    foreign key (pou_isa_po)
        references PostOggetto(id)
    condizione Condizione not null,
    anni_garanzia IntGEZ not null
);

create table VenditoreProf(
    vp_isa_ut Stringa primary key,
    foreign key (vp_isa_ut)
        references Utente(username),
    vetrina URL not null,
    unique(vetrina)
);

create table PostOggettoNuovo(
    pon_isa_po serial primary key,
    foreign key (pon_isa_po)
        references PostOggetto(id),
    anni_garanzia IntG1 not null,
    pubblica_nuovo Stringa not null,
    foreign key pubblica_nuovo
        references VenditoreProf(vp_isa_ut)
);

create table Privato(
    pr_isa_ut Stringa primary key,
    foreign key (pr_isa_ut)
        references Utente(username)
);

create table Asta(
    asta_isa_po serial primary key,
    foreign key (asta_isa_po)
        references PostOggetto(id),
    prezzo_base RealGEZ not null,
    prezzo_bid RealGZ not null,
    scadenza timestamp not null
);

create table Bid(
    codice serial primary key,
    istante timestamp not null,
    asta_bid serial not null,
    unique(istante, asta_bid),
    foreign key asta_bid
        references Asta(asta_isa_po)
);

create table CompraloSubito(
    cs_isa_po serial primary key
    foreign key cs_isa_po
        references PostOggetto(id),
    prezzo RealGZ not null,
    istante_aquirente timestamp
);