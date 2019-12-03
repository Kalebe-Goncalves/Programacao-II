use locadora;

select cliente.nom_cliente,
dependente.nom_dependente from cliente
INNER JOIN dependente on dependente.cod_cliente=cliente.cod_cliente;

SELECT filme.nom_filme, genero.den_genero, categoria.den_categoria
FROM filme
INNER JOIN genero USING (cod_genero)
INNER JOIN categoria USING (cod_categoria);

SELECT filme.nom_filme, ator.nom_ator, tipo_atuacao.den_tip_atuacao
FROM elenco
INNER JOIN ator USING (cod_ator)
INNER JOIN filme USING (cod_filme)
INNER JOIN tipo_atuacao USING (cod_tip_atuacao); 

SELECT filme.nom_filme, COUNT(tipo_midia.den_tip_midia) as "quantidade de midias existentes"
FROM midia_filme
INNER JOIN filme USING (cod_filme)
INNER JOIN tipo_midia USING (cod_tip_midia)
GROUP BY nom_filme;

SELECT COUNT(midia_filme.cod_midia)
FROM midia_filme
INNER JOIN tipo_midia USING (cod_tip_midia)
GROUP BY cod_tip_midia;

SELECT cliente.nom_cliente, count(dependente.cod_dependente)
FROM cliente
INNER JOIN dependente USING (cod_cliente)
GROUP BY nom_cliente;

SELECT COUNT(filme.cod_filme)
FROM filme
INNER JOIN genero USING (cod_genero)
GROUP BY cod_genero;

SELECT filme.nom_filme, midia_filme.cod_midia, den_tip_midia
FROM midia_filme
INNER JOIN filme USING (cod_filme)
INNER JOIN tipo_midia USING (cod_tip_midia)
GROUP BY cod_midia;