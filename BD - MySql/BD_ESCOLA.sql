CREATE DATABASE Escola CHARSET = latin1 COLLATE latin1_general_cs;

CREATE TABLE Curso(
id_curso INT NOT NULL PRIMARY KEY,
nom_curso VARCHAR(100),
carga_horaria VARCHAR(10)
);

CREATE TABLE Turma(
id_turma INT NOT NULL PRIMARY KEY,
nom_turma INT,
desc_ano VARCHAR(20),
id_curso INT NOT NULL,
FOREIGN KEY (id_curso) REFERENCES Curso
);

CREATE TABLE Aluno(
num_matricula INT NOT NULL PRIMARY KEY,
nom_aluno VARCHAR(100),
genero VARCHAR(1),
id_turma INT NOT NULL,
FOREIGN KEY (id_turma) REFERENCES Turma
);

CREATE TABLE Disciplina(
cod_disciplina INT NOT NULL PRIMARY KEY,
nom_disciplina VARCHAR(50),
carga_horaria INT,
cod_professor INT NOT NULL,
FOREIGN KEY (cod_professor) REFERENCES Professor
);

CREATE TABLE GradeDisciplinas(
id_turma INT NOT NULL,
cod_disciplina INT NOT NULL,
FOREIGN KEY (id_turma) REFERENCES Turma,
FOREIGN KEY (cod_disciplina) REFERENCES Disciplina
);

CREATE TABLE Professor(
cod_professor INT NOT NULL PRIMARY KEY,
nom_professor VARCHAR(50),
desc_func VARCHAR(20)
);


INSERT INTO Curso (id_curso, nom_curso, carga_horaria) VALUES (01, "Curso Técnico Integrado de Informática", "400 Horas");
INSERT INTO Curso (id_curso, nom_curso, carga_horaria) VALUES (02, "Curso Técnico Integrado de Eletromecânica", "400 Horas");

INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (001, 101, "Primeiro", 01);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (002, 102, "Primeiro", 01);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (003, 201, "Segundo", 01);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (004, 202, "Segundo", 01);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (005, 301, "Terceirão", 01);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (006, 302, "Terceirão", 01);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (011, 101, "Primeiro", 02);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (012, 102, "Primeiro", 02);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (013, 201, "Segundo", 02);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (014, 202, "Segundo", 02);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (015, 301, "Terceirão", 02);
INSERT INTO Turma (id_turma, nom_turma, desc_ano, id_curso) VALUES (016, 302, "Terceirão", 02);

INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190001,	'Ana Cristina A.de Alencar',"F", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190002,	'Andréa Cristina dos Santos Corrêa',"F", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190003,	'Altair de Souza Caldas',"M", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190004,	'Áurea Regina Meira',"F", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190005,	'Antonia Farias Costa Sousa',"F", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190006,	'Adriana Mendes Ribeiro',"F", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190007,	'Cinthia Nazaré Maciel da Cruz',"F", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190008,	'Roberto Júnior C. Pother',"M", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190009,	'Urubatan Nazaré Anacleto de Paiva',"M", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190010,	'Simei Nascimento da Silva',"M", 001);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190011,	'Gabriella Franco',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190012,	'Adelson Vivaldo Siqueira Junior',"M", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190013,	'Ana Clara Do Valle',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190014,	'Anni Gabrieli Da Silva',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190015,	'Beatriz Laureano De Souza',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190016,	'Bianca Cristina Domingos',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190017,	'Bianca Rocha Amaragi ',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190018,	'Dienifer Da Silva Gonçalves',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190019,	'Gabriéli Oliveira Santos ',"F", 002);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20190020,	'Giovani Henrique Do Nascimento De Jesus',"M", 002);

INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180001,	'Bruno De Lucas Santos Silva',"M", 013);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180002,	'Caio Lopes Neves ',"M", 013);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180003,	'Caroline Lauriano Silva ',"F", 013);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180004,	'Augusto Henrique Piva',"M", 013);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180005,	'Guilherme Theodoro Veronesi ',"M", 013);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180006,	'Hugo Da Silva Victório',"M", 013);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180011,	'Jeici Cristina Germano',"F", 014);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180012,	'Joyce Rosalina Pires',"F", 014);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180013,	'Matheus Junior De Oliveira ',"M", 014);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20180014,	'Wladimir Galdino De Lima Bonfim',"M", 014);

INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170001,	'Luiz Antonio da Silva Lopes',"M", 005);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170002,	'Kalebe Bognar Gonçalves',"M", 005);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170003,	'Gabriel Rosa Schmidt',"M", 005);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170004,	'Felipe Augusto Fiamoncini',"M", 005);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170011,	'Carlos Henrique de Morais',"M", 006);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170012,	'Gabriel Eduardo Germano',"M", 006);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170013,	'Matheus Henrique Testoni dos Santos',"M", 006);
INSERT INTO Aluno (num_matricula, nom_aluno, genero, id_turma) VALUES (20170015,	'Bernado Zonta Luckmann',"M", 006);

INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (1, "Adaltro Prochnov Nunes", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (2, "Aldelir Fernando Luiz", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (3, "Helenice Nazaré da Cunha Silva", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (4, "Anderson Nereu Galcowski", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (5, "Cloves Alexandre de Castro", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (6, "Cláudia Zimmer de Cerqueira Cezar", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (7, "Deusis Elton Schlickmann Frainer", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (8, "Edinho Augusto Penharbel", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (9, "Cássia Aline Schuck", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (10, "Luiz Ricardo Uriarte", "Docente");
INSERT INTO Professor (cod_professor, nom_professor, desc_func) VALUES (11, "Karlan Rau", "Docente");

INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (00, "Filosofia", 1, 1);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (01, "Banco de Dados", 67, 2);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (10, "Português", 55, 3);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (11, "História", 20, 4);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (100, "Geografia", 40, 5);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (101, "Artes", 78, 6);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (110, "Educação Física", 24, 7);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (111, "Lógica de Programação", 110, 8);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (1000, "Matemática", 40, 9);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (1001, "Engenharia de Software", 12, 10);
INSERT INTO Disciplina (cod_disciplina, nom_disciplina, carga_horaria, cod_professor) VALUES (1010, "Biologia", 43, 11);

INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (001, 00);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (001, 01);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (001, 10);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (002, 11);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (002, 100);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (002, 101);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (003, 110);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (003, 111);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (003, 1000);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (004, 1001);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (004, 1010);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (004, 00);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (005, 01);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (005, 10);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (005, 11);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (006, 100);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (006, 101);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (006, 110);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (011, 111);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (011, 1000);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (011, 1001);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (012, 1010);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (012, 00);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (012, 01);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (013, 10);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (013, 11);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (013, 100);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (014, 101);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (014, 110);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (014, 111);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (015, 1000);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (015, 1001);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (015, 1010);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (016, 01);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (016, 10);
INSERT INTO GradeDisciplinas (id_turma, cod_disciplina) VALUES (016, 11);

CREATE VIEW v_AlunoDisciplina AS
SELECT count(a.num_matricula)
FROM Aluno a INNER JOIN Turma
USING (id_turma)
INNER JOIN GradeDisciplinas gd
USING (id_turma)
INNER JOIN Disciplina
USING (cod_disciplina)
WHERE cod_disciplina = 00
;

select * from v_AlunoDisciplina;














