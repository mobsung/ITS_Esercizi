create table docente(
    mat integer primary key,
    nome varchar(100) not null,
    cognome varchar(100) not null,
    email varchar(100) not null
);


create table corso(
    codice integer primary key,
    nome varchar not null,
    aula varchar(100) not null
);


create table incarico(
    docente integer not null,
    corso integer not null,
    primary key(docente, corso),
    foreign key(docente)
        references docente(mat),
    foreign key(corso)
        references corso(codice)
);

-- docker exec -it its_postgresql bash
-- psql -U postgres