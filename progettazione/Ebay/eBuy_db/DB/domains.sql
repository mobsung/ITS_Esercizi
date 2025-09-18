CREATE DOMAIN stringa AS varchar;
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