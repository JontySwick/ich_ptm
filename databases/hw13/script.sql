-- Написать запросы по созданию таблиц со связями и ключами на основе получившейся ER-диаграммы службы такси.
CREATE SCHEMA german_taxi
USE german_taxi;

CREATE TABLE masters
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    first_name   VARCHAR(50) NOT NULL,
    last_name    VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE procedures
(
    id             INT PRIMARY KEY AUTO_INCREMENT,
    procedure_name VARCHAR(250) NOT NULL UNIQUE
);

CREATE TABLE procedures_to_masters
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    procedure_id INT,
    master_id    INT,
    FOREIGN KEY (master_id) REFERENCES masters (id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures (id) ON DELETE CASCADE
);

CREATE TABLE auto_park
(
    id   int primary key auto_increment,
    name varchar(255) not null unique
);

CREATE TABLE auto_type
(
    id   INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE drivers
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    first_name   VARCHAR(50) NOT NULL,
    last_name    VARCHAR(50) NOT NULL,
    sex          ENUM ('MALE', 'FEMALE'),
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE auto
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    vin          CHAR(17) UNIQUE,
    brand        VARCHAR(255) NOT NULL,
    model        VARCHAR(255) NOT NULL,
    number       VARCHAR(10)  NOT NULL,
    color        VARCHAR(55)  NOT NULL,
    auto_park_id int,
    auto_type_id int,
    driver_id    int          not null unique,
    FOREIGN KEY (auto_park_id) REFERENCES auto_park (id),
    FOREIGN KEY (auto_type_id) REFERENCES auto_type (id),
    FOREIGN KEY (driver_id) REFERENCES drivers (id)
);

CREATE TABLE sto
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    auto_id      INT      NOT NULL,
    auto_park_id INT      NOT NULL,
    procedure_id INT      NOT NULL,
    date_start   DATETIME NOT NULL,
    date_finish  DATETIME,
    FOREIGN KEY (procedure_id) REFERENCES procedures (id),
    FOREIGN KEY (auto_id) REFERENCES auto (id),
    FOREIGN KEY (auto_park_id) REFERENCES auto_park (id)
);

CREATE TABLE review
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    rating  TINYINT UNSIGNED NOT NULL CHECK (rating BETWEEN 0 AND 100),
    comment text
);

CREATE TABLE clients
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    first_name   VARCHAR(50) NOT NULL,
    last_name    VARCHAR(50),
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE addresses
(
    id     INT PRIMARY KEY AUTO_INCREMENT,
    street VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE orders
(
    id             INT PRIMARY KEY AUTO_INCREMENT,
    review_id      INT      NOT NULL,
    client_id      INT      NOT NULL,
    driver_id      INT      NOT NULL,
    auto_id        INT      NOT NULL,
    cost           FLOAT    NOT NULL,
    create_date    DATETIME NOT NULL,
    start_date     DATETIME,
    finish_date    DATETIME,
    start_address  int,
    finish_address int,
    FOREIGN KEY (client_id) REFERENCES clients (id),
    FOREIGN KEY (driver_id) REFERENCES drivers (id),
    FOREIGN KEY (auto_id) REFERENCES auto (id),
    FOREIGN KEY (review_id) REFERENCES review (id),
    FOREIGN KEY (start_address) REFERENCES addresses (id),
    FOREIGN KEY (finish_address) REFERENCES addresses (id)
);