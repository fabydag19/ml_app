CREATE TABLE users (
    id int auto_increment primary key not null,
    username varchar(255) unique not null,
    password_hash varchar(255) not null,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    is_active boolean default true,
    activation_date datetime default current_timestamp,
    deactivation_date datetime,
    last_login datetime
);

INSERT INTO users (username, password_hash, first_name, last_name, is_active, activation_date)
VALUES (
    'mrossi', 
    SHA2('mrossi', 256), 
    'Mario', 
    'Rossi', 
    true, 
    NOW()
);