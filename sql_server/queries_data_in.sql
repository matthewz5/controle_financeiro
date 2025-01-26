-- lendo a base de dados
SELECT * FROM data_in

-- somando o valor total
SELECT SUM(valor) FROM data_in

-- agrupando pro mes
SELECT 
    DATE_TRUNC('month', data) AS mes, 
    SUM(valor) AS total_valor
FROM 
    data_in
GROUP BY 
    mes
ORDER BY 
    mes;

-- agrupe o valor por origem
SELECT 
    origem, 
    SUM(valor) AS total_valor
FROM 
    data_in
GROUP BY 
    origem
ORDER BY 
    total_valor DESC;

-- agrupando por mes e origem
SELECT 
    DATE_TRUNC('month', data) AS mes, 
    origem, 
    SUM(valor) AS total_valor
FROM 
    data_in
GROUP BY 
    mes, origem
ORDER BY 
    mes, total_valor ASC;

-- 5 maiores entradas
SELECT 
    origem, 
	categoria,
    valor
FROM 
    data_in
ORDER BY 
    valor DESC
LIMIT 5;

-- total de registros por origem
SELECT 
    origem, 
    COUNT(*) AS total_registros
FROM 
    data_in
GROUP BY 
    origem
ORDER BY 
    total_registros DESC;