create domain PosInteger as Integer
    check ( value >= 0 );

create domain StringaM as varchar(100);

create domain CodIATA as char(3);

create table Compagnia(
    nome StringaM primary key,
    annoFondaz PosInteger
);

create table Volo(
    codice PosInteger not null,
    comp StringaM not null,
    primary key(codice, comp),
    durataMinuti PosInteger not null,
    foreign key (comp) references Compagnia(nome)
);

create table Aeroporto(
    codice CodIATA primary key,
    nome StringaM not null
);

create table ArrPart(
    codice PosInteger not null,
    comp StringaM not null,
    primary key(codice, comp),
    arrivo CodIATA not null,
    partenza CodIATA not null,
    foreign key (codice, comp) references Volo(codice, comp) deferrable,
    foreign key (arrivo) references Aeroporto(codice),
    foreign key (partenza) references Aeroporto(codice)
);


create table LuogoAeroporto(
    aeroporto CodIATA primary key,
    citta StringaM not null,
    nazione StringaM not null,
    foreign key (aeroporto) references Aeroporto(codice) deferrable
);

alter table Volo
add constraint fk_volo_arrpart
foreign key (codice, comp)
references ArrPart(codice, comp) deferrable;

alter table Aeroporto
add constraint fk_aeroporto_luogoaeroporto
foreign key (codice) 
references LuogoAeroporto(aeroporto) deferrable;