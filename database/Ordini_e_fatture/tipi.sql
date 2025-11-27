create domain Stringa as varchar;

create domain PartitaIVA as char(11)
        check (value ~ '^[0-9]{11}$');

create domain CodiceFiscale as char(16)
        check (value ~'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

create domain EMail as varchar
        check (value ~ '^[\w\.-]+@[\w\.-]+\.\w{2,}$');

create domain Telefono as varchar(20);

create domain IntGEZ as Integer
        check (value >= 0);

create domain RealGEZ as Real
        check (value >= 0);

create domain RealI01
        check (value  > 0 and value < 1);

creater type Indirizzo as(
        via varchar,
        civico varchar,
        cap char(5)
);

create type stato as 
    enum ('in preparazione', 'inviato', 'da saldare', 'saldato');
