DELIMITER $

CREATE FUNCTION mdc(a int, b int)
returns int
BEGIN
    DECLARE resto INT default 0;
    loopzao:LOOP
    SET resto = a%b;
    IF resto = 0 THEN LEAVE loopzao;
    END IF;
    SET a = b;
    SET b = resto;
    END LOOP loopzao;
return b;
END $

DELIMITER $

CREATE PROCEDURE mmc(IN a INT, IN b INT, OUT r INT)
BEGIN
    DROP TABLE IF EXISTS teste;
    CREATE TABLE teste(
        numero INT PRIMARY KEY
    );
    INSERT INTO teste VALUE (a*b/mdc(a,b));
    SELECT * FROM teste;
END $

DELIMITER $

CREATE PROCEDURE palindromo(IN a VARCHAR(255), OUT r BOOL)
BEGIN
    DROP TABLE IF EXISTS teste;
    CREATE TABLE teste(
        palindromo BOOLEAN PRIMARY KEY,
        binario VARCHAR(15)
    );
    IF a = REVERSE(a) THEN
        INSERT INTO teste VALUES (TRUE, 'Verdade');
    ELSE
        INSERT INTO teste VALUES (FALSE, 'Falso');
    END IF;
    SELECT binario FROM teste;
    
END $

call palindromo("teste", @total);
call palindromo("ovo", @total);


SELECT mdc(48,30) as resultado;
CALL mmc(40, 38, @total);
