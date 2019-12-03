
DROP DATABASE IF EXISTS locadora;

CREATE SCHEMA locadora CHARACTER SET latin1 COLLATE latin1_general_cs;

USE locadora;

CREATE TABLE ator (
    cod_ator INTEGER NOT NULL PRIMARY KEY,
    nom_ator VARCHAR(40)
);

 
CREATE TABLE categoria (
    cod_categoria INTEGER NOT NULL PRIMARY KEY,
    den_categoria VARCHAR(40),
    val_locacao DECIMAL(10,2),
    qtd_dias INTEGER
);


CREATE TABLE genero (
    cod_genero INTEGER NOT NULL PRIMARY KEY,
    den_genero VARCHAR(40)
);


CREATE TABLE filme (
    cod_filme        INTEGER NOT NULL PRIMARY KEY,
    nom_filme        VARCHAR(40),
    cod_categoria    INTEGER,
    cod_genero       INTEGER,
    nom_diretor      VARCHAR(20),
    dat_ano_producao YEAR,
    cod_predecessor  INTEGER,
    ind_remake       BOOL,
    ind_sequencia    BOOL,
    foreign key (cod_categoria) references categoria (cod_categoria) on delete cascade,
    foreign key (cod_genero) references genero (cod_genero) on delete cascade,
    foreign key (cod_predecessor) references filme (cod_filme) on delete cascade
);


CREATE TABLE cliente (
    cod_cliente INTEGER NOT NULL PRIMARY KEY,
    nom_cliente VARCHAR(60),
    ind_ativo   ENUM('A', 'I')
);

CREATE TABLE dependente (
    cod_dependente INTEGER NOT NULL PRIMARY KEY,
    nom_dependente VARCHAR(40),
    cod_cliente INTEGER,
    foreign key (cod_cliente) references cliente (cod_cliente) on delete cascade
);
 

CREATE TABLE tipo_atuacao (
    cod_tip_atuacao INTEGER PRIMARY KEY,
    den_tip_atuacao VARCHAR(30) NOT NULL
);


CREATE TABLE elenco (
    cod_ator  INTEGER NOT NULL,
    cod_filme INTEGER NOT NULL,
    cod_tip_atuacao  INTEGER NOT NULL,
    primary key (cod_ator, cod_filme),
    foreign key (cod_ator) references ator (cod_ator) on delete cascade,
    foreign key (cod_filme) references filme (cod_filme) on delete cascade,
    foreign key (cod_tip_atuacao) references tipo_atuacao (cod_tip_atuacao) on delete cascade
);


CREATE TABLE tipo_midia (
    cod_tip_midia INTEGER NOT NULL PRIMARY KEY,
    den_tip_midia VARCHAR(10)
);


CREATE TABLE midia_filme (
    cod_midia INTEGER NOT NULL PRIMARY KEY,
    cod_filme INTEGER,
    cod_tip_midia INTEGER,
    den_formato VARCHAR(15),
    foreign key (cod_filme) references filme (cod_filme) on delete cascade,
    foreign key (cod_tip_midia) references tipo_midia (cod_tip_midia) on delete cascade
);

 
CREATE TABLE locacao (
    cod_locacao INTEGER NOT NULL PRIMARY KEY,
    dat_locacao DATE,
    dat_prv_devolucao  DATE,
    cod_cliente INTEGER NOT NULL,
    foreign key (cod_cliente) references cliente (cod_cliente) on delete cascade
);


CREATE TABLE item_locacao (
    cod_midia INTEGER NOT NULL,
    cod_locacao INTEGER NOT NULL,
    val_locacao NUMERIC(10,2),
    dat_devolucao DATE,
    primary key (cod_midia, cod_locacao),
	  foreign key (cod_midia) references midia_filme (cod_midia) on delete cascade,
    foreign key (cod_locacao) references locacao (cod_locacao) on delete cascade
);

 
CREATE TABLE historico_locacao (
    cod_locacao INTEGER NOT NULL PRIMARY KEY,
    dat_locacao DATE NOT NULL,
    dat_prv_devolucao  DATE,
    cod_cliente INTEGER NOT NULL,
    foreign key (cod_cliente) references cliente (cod_cliente) on delete cascade
);



INSERT INTO ator (cod_ator, nom_ator) VALUES (1, 'Amazonino Hurt');
INSERT INTO ator (cod_ator, nom_ator) VALUES (2, 'Petrúcio Drakker');
INSERT INTO ator (cod_ator, nom_ator) VALUES (3, 'Madalena Shaw');
INSERT INTO ator (cod_ator, nom_ator) VALUES (4, 'Zenoveva Star');
INSERT INTO ator (cod_ator, nom_ator) VALUES (5, 'Veneravez Crow');
INSERT INTO ator (cod_ator, nom_ator) VALUES (6, 'Aparício Liss');
INSERT INTO ator (cod_ator, nom_ator) VALUES (7, 'Amarílis Berth');
INSERT INTO ator (cod_ator, nom_ator) VALUES (8, 'Pedrita Bedrock');
INSERT INTO ator (cod_ator, nom_ator) VALUES (9, 'Magnólia Petersen');
INSERT INTO ator (cod_ator, nom_ator) VALUES (10, 'Arianna Listhon');
INSERT INTO ator (cod_ator, nom_ator) VALUES (11, 'Maryah Lenning');
INSERT INTO ator (cod_ator, nom_ator) VALUES (12, 'Blondie Barret');
INSERT INTO ator (cod_ator, nom_ator) VALUES (13, 'Anastácia Ray');
INSERT INTO ator (cod_ator, nom_ator) VALUES (14, 'Penelope Cross');
INSERT INTO ator (cod_ator, nom_ator) VALUES (15, 'Ryan Gosling');
INSERT INTO ator (cod_ator, nom_ator) VALUES (16, 'Harrison Ford');
INSERT INTO ator (cod_ator, nom_ator) VALUES (17, 'Rami Malek');
INSERT INTO ator (cod_ator, nom_ator) VALUES (18, 'Mark Hamill');
INSERT INTO ator (cod_ator, nom_ator) VALUES (19, 'Ray Deckerd');


  
INSERT INTO categoria (cod_categoria, den_categoria, val_locacao, qtd_dias) VALUES (1, 'Lançamento', 3.50, 2);
INSERT INTO categoria (cod_categoria, den_categoria, val_locacao, qtd_dias) VALUES (2, 'Pós-Lançamento', 2.50, 3);
INSERT INTO categoria (cod_categoria, den_categoria, val_locacao, qtd_dias) VALUES (3, 'Catálogo', 1.50, 4);
INSERT INTO categoria (cod_categoria, den_categoria, val_locacao, qtd_dias) VALUES (4, 'Antigo', 1.00, 5);
INSERT INTO categoria (cod_categoria, den_categoria, val_locacao, qtd_dias) VALUES (5, 'Pré-Lançamento', 7.00, 1);


INSERT INTO tipo_atuacao (cod_tip_atuacao, den_tip_atuacao) VALUES (1, 'Protagonista'), (2, 'Co-protagonista'), (3, 'Antagonista'), (4, 'Oponente'), (5, 'Coadjuvante'), (6, 'Figurante');


INSERT INTO genero (cod_genero, den_genero) VALUES (1, 'Comédia');
INSERT INTO genero (cod_genero, den_genero) VALUES (2, 'Drama');
INSERT INTO genero (cod_genero, den_genero) VALUES (3, 'Ação');
INSERT INTO genero (cod_genero, den_genero) VALUES (4, 'Aventura');
INSERT INTO genero (cod_genero, den_genero) VALUES (5, 'Documentário');
INSERT INTO genero (cod_genero, den_genero) VALUES (6, 'Religioso');
INSERT INTO genero (cod_genero, den_genero) VALUES (7, 'Ficção');
INSERT INTO genero (cod_genero, den_genero) VALUES (8, 'Infantil'); 
INSERT INTO genero (cod_genero, den_genero) VALUES (9, 'Terror');
INSERT INTO genero (cod_genero, den_genero) VALUES (10, 'TV/Seriado');
INSERT INTO genero (cod_genero, den_genero) VALUES (11, 'Filmes HQ');
INSERT INTO genero (cod_genero, den_genero) VALUES (12, 'Romance');
INSERT INTO genero (cod_genero, den_genero) VALUES (13, 'Épico');
INSERT INTO genero (cod_genero, den_genero) VALUES (14, 'Educativo');
INSERT INTO genero (cod_genero, den_genero) VALUES (15, 'Musical');


INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (1, 'Máquina Mortifera', 1, 3, 'Mel Gibson', 1986);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (2, 'Toy Story', 2, 8, 'Tony Martin', 2005);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (3, 'Missão Impossível', 1, 7, 'Bradley Cooper', 1998);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (4, 'Rambo II: a missão', 1, 2, 'Zack Snyder', 1982);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (5, 'O Exterminador do Futuro', 3, 3, 'James Cameron', 1984);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (6, 'O Exorcista', 3, 9, 'James Cameron', 1970);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (7, 'E o Vento Levou', 4, 12, 'Alfred Hitcock', 1955);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (8, 'King Kong', 4, 4, 'McG', 1977);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (9, 'Velozes e Furiosos 7', 1, 3, 'Justin Lin', 2015);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (10, 'Dexter', 3, 10, 'Michael C. Hall', 2006);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (11, 'Homeland', 3, 10, 'James Cameron', 2011);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (12, 'Capitão América: Guerra Civil', 1, 3, 'Kevin Fiege', 2016);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (13, 'Batman Vs. Superman: A origem da Justiça', 1, 11, 'Zack Snyder', 2016);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (14, 'A grande aposta', 2, 2, 'Mel Gibson', 2014);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (15, 'O lobo de Wall Street', 3, 2, 'Bradley Cooper', 2012);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (16, 'Mr. Robot', 1, 10, 'Michael C. Hall', 2015);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (17, 'Morro dos ventos uivantes', 3, 12, 'Willian Hurt', 1955);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (18, 'Ben Hur', 3, 13, 'Charlton Reston', 1963);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (19, 'Contos da Cripta', 3, 9, 'Stephen King', 1989);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (20, 'A fantástica fábrica de chocolates', 3, 1, 'Willian Hurt', 2007);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (21, 'Cemitério Maldito', 3, 9, 'Stephen King', 1989);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (22, 'Breaking Bad', 3, 10, 'Vince Gilligan', 2008);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (23, 'Desejo de Matar', 2, 2, 'Bruce Willians', 1981);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (24, 'Vingadores: Gerra Infinita', 1, 3, 'Joe Russo', 2017);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (25, 'Bohemian Rhapsody', 5, 2, 'Bryan Singer', 2018);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (26, 'Blade Runner 2049', 2, 4, 'Denis Villeneuve', 2017);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (27, 'Star Wars: Os Últimos Jedi', 2, 7, 'J. J. Abrams', 2017);
INSERT INTO filme (cod_filme, nom_filme, cod_categoria, cod_genero, nom_diretor, dat_ano_producao) VALUES (28, 'AC/DC Let There Be Rock', 2, 15, 'George Young', 1980);



INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (1, 1, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (1, 2, 3);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (2, 1, 5);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (2, 3, 6);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (2, 4, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (3, 5, 4);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (3, 6, 6);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (4, 7, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (4, 8, 4);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (5, 8, 5);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (6, 9, 6);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (7, 8, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (8, 13, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (14, 21, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (12, 18, 6);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (9, 20, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (13, 16, 5);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (11, 12, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (19, 24, 2);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (15, 26, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (16, 26, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (17, 25, 1);
INSERT INTO elenco (cod_ator, cod_filme, cod_tip_atuacao) VALUES (18, 27, 6);


INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (1, 'Babilonio', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (2, 'Anacleto', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (3, 'Marivalda', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (4, 'Gervasio', 'I');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (5, 'Zenoveva', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (6, 'Gumercinda', 'I');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (7, 'Ambarina', 'I');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (8, 'Mafaldo', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (9, 'Jumerlau', 'I');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (10, 'Maneco', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (11, 'Veneravez', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (12, 'Percivaldo', 'I');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (13, 'Amarílis', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (14, 'Bene', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (15, 'Valêncio', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (16, 'Demóstenes', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (17, 'Perovânia', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (18, 'Aparícia', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (19, 'Ambrósia', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (20, 'Heisenberg', 'A');
INSERT INTO cliente (cod_cliente, nom_cliente, ind_ativo) VALUES (21, 'Djeberson', 'A');



INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (0, 'Alexandre', 10);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (1, 'Jose', 1);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (2, 'Pedro', 1);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (3, 'Antonio', 1);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (4, 'Jose Maria', 2);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (5, 'Mariana', 2);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (6, 'Joel', 3);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (7, 'Pedro Antonio', 4);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (8, 'Maria Antonia', 4);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (9, 'Maria Angelica', 4);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (10, 'Angela', 5);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (11, 'Maria', 5);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (12, 'Pedro', 5);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (13, 'Antonio', 5);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (14, 'Luiz', 5);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (15, 'Cesar', 6);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (16, 'Abel', 6);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (17, 'Marcos', 7);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (18, 'Marco Antonio', 7);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (19, 'Pedro Henrique', 8);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (20, 'Alexandre', 12);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (21, 'Henrique', 12);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (22, 'Beatriz', 14);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (23, 'Luciana', 14);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (24, 'Elias', 10);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (25, 'Luis Pedro', 10);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (27, 'Luis Pedro', 10);
INSERT INTO dependente (cod_dependente, nom_dependente, cod_cliente) VALUES (28, 'Luis Pedro', 10);


INSERT INTO tipo_midia (cod_tip_midia, den_tip_midia) VALUES (1, 'VHS');
INSERT INTO tipo_midia (cod_tip_midia, den_tip_midia) VALUES (2, 'DVD');
INSERT INTO tipo_midia (cod_tip_midia, den_tip_midia) VALUES (3, 'BluRay');
INSERT INTO tipo_midia (cod_tip_midia, den_tip_midia) VALUES (4, 'LaserDisc');
INSERT INTO tipo_midia (cod_tip_midia, den_tip_midia) VALUES (5, 'Digital');


INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (1, 1, 1, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (2, 1, 1, 'DUBLADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (3, 2, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (4, 2, 1, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (5, 3, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (6, 3, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (7, 4, 4, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (8, 4, 1, 'DUBLADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (9, 4, 1, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (10, 5, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (11, 6, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (12, 7, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (13, 8, 4, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (14, 9, 5, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (15, 10, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (16, 11, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (17, 12, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (18, 13, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (19, 14, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (20, 15, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (21, 16, 5, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (22, 17, 1, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (23, 18, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (24, 19, 5, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (25, 20, 4, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (26, 21, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (27, 21, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (28, 20, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (29, 22, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (30, 22, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (31, 22, 5, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (32, 23, 5, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (33, 24, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (34, 24, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (35, 25, 5, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (36, 26, 1, 'LEGENDADO');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (37, 26, 4, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (38, 26, 2, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (39, 27, 3, '--');
INSERT INTO midia_filme (cod_midia, cod_filme, cod_tip_midia, den_formato) VALUES (40, 27, 4, '--');


INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (1, '2018-01-25', 20);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (2, '2017-05-31', 17);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (3, now(), 15);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (4, now(), 16);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (5, '2017-10-21', 20);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (6, '2017-09-26', 18);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (7, now(), 19);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (8, '2014-12-13', 20);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (9, '2011-03-01', 13);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (10, '2003-01-10', 1);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (11, '2003-02-10', 2);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (12, '2010-03-10', 3);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (13, '2003-04-10', 1);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (14, '2001-09-10', 2);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (15, '2003-06-10', 2);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (16, '2012-06-15', 3);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (17, '2007-03-21', 4);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (18, '2003-07-21', 5);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (19, '2014-04-21', 6);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (20, '2003-06-21', 2);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (21, '2015-07-22', 2);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (22, '2003-07-22', 3);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (23, '2002-07-22', 8);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (24, '2000-10-12', 9);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (25, '2001-08-15', 7);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (26, '2015-08-15', 12);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (27, '2016-10-25', 14);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (28, '2016-10-21', 11);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (29, '2018-12-06', 16);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (30, '2018-12-07', 19);
INSERT INTO locacao (cod_locacao, dat_locacao, cod_cliente) VALUES (31, '2018-12-01', 18);


INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 11, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 12, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 15, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 18, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 19, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 21, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (2, 10, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (2, 14, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (2, 17, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (2, 20, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (2, 25, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (3, 12, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (3, 13, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (3, 16, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (3, 19, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (3, 22, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (4, 12, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (4, 14, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (4, 17, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (4, 20, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (5, 16, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (5, 19, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (5, 23, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (6, 13, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (6, 14, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (6, 17, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (7, 17, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (7, 18, 4.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (8, 24, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (2, 27, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (29, 1, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (13, 1, 2.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (29, 2, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (30, 3, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (17, 3, 2.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (1, 3, 1.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (31, 5, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (32, 8, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (21, 11, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (25, 10, 3.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (8, 6, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (11, 7, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (25, 9, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (22, 4, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (33, 29, 7.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (36, 29, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (40, 30, 8.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (34, 30, 5.00, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (37, 31, 2.50, NULL);
INSERT INTO item_locacao (cod_midia, cod_locacao, val_locacao, dat_devolucao) VALUES (35, 31, 1.50, NULL);




UPDATE item_locacao SET dat_devolucao = (SELECT date_add(dat_locacao, interval 1+floor(rand()*7) day)
                                           FROM locacao
                                          WHERE item_locacao.cod_locacao = locacao.cod_locacao);


UPDATE locacao SET dat_prv_devolucao = date_add(dat_locacao, interval 5 day);

-- Letra B
	

CREATE TABLE alditoria_elenco(
	cod_ator INT NOT NULL,
	acao VARCHAR(30) NOT NULL
);

DELIMITER $
CREATE TRIGGER t_add_alditoria_elenco AFTER INSERT ON elenco
FOR EACH ROW
BEGIN
	INSERT INTO alditoria_elenco VALUES(new.cod_ator,"Adicionado");
END $

DELIMITER $
CREATE TRIGGER t_rem_alditoria_elenco AFTER DELETE ON elenco
FOR EACH ROW
BEGIN
	INSERT INTO alditoria_elenco VALUES(old.cod_ator,"Removido");
END $

INSERT INTO elenco VALUES(2,2,1);
DELETE FROM elenco WHERE cod_ator = 2 and cod_filme = 2;

SELECT * FROM alditoria_elenco;

CREATE TABLE registro_atrasos(
	id_cliente INT PRIMARY KEY,
	qtd_atrasos INT NOT NULL
);

INSERT INTO registro_atrasos SELECT cod_cliente,0 from cliente;
SELECT * FROM registro_atrasos;

-- Letra C


DELIMITER $
CREATE TRIGGER t_registrar_atraso AFTER INSERT ON item_locacao
FOR EACH ROW
BEGIN

	DECLARE dat_prevista DATE DEFAULT NULL;
	DECLARE cliente INT DEFAULT NULL;

	SELECT dat_prv_devolucao INTO dat_prevista FROM locacao where locacao.cod_locacao = new.cod_locacao;
	SELECT cod_cliente INTO cliente FROM locacao where locacao.cod_locacao = new.cod_locacao;

	IF dat_prevista < new.dat_devolucao THEN
		UPDATE registro_atrasos SET qtd_atrasos = qtd_atrasos + 1 WHERE id_cliente = cliente;
	END IF;


END $

select * from registro_atrasos
ORDER BY id_cliente DESC
;
INSERT INTO locacao VALUES(36,'2019-10-20','2019-10-20',2);
INSERT INTO item_locacao VALUES(2,36,10.8,'2020-10-20');
	








