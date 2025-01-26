SELECT * FROM data_out

-- soma de valores
SELECT 
    SUM(valor) AS total_valor
FROM 
    data_out;

-- Soma de valores total por mês, ordenando pelo mês

SELECT 
    DATE_TRUNC('month', data) AS mes, 
    SUM(valor) AS total_valor
FROM 
    data_out
GROUP BY 
    mes
ORDER BY 
    mes;

-- Top 10 categorias com maior valor

SELECT 
    categoria, 
    SUM(valor) AS total_valor
FROM 
    data_out
GROUP BY 
    categoria
ORDER BY 
    total_valor DESC
LIMIT 10;

-- Valor médio das categorias por mês, com cada categoria em uma coluna
SELECT 
    categoria,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 1 THEN valor ELSE 0 END) AS janeiro,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 2 THEN valor ELSE 0 END) AS fevereiro,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 3 THEN valor ELSE 0 END) AS marco,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 4 THEN valor ELSE 0 END) AS abril,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 5 THEN valor ELSE 0 END) AS maio,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 6 THEN valor ELSE 0 END) AS junho,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 7 THEN valor ELSE 0 END) AS julho,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 8 THEN valor ELSE 0 END) AS agosto,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 9 THEN valor ELSE 0 END) AS setembro,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 10 THEN valor ELSE 0 END) AS outubro,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 11 THEN valor ELSE 0 END) AS novembro,
    SUM(CASE WHEN EXTRACT(MONTH FROM data) = 12 THEN valor ELSE 0 END) AS dezembro
FROM 
    data_out
GROUP BY 
    categoria
ORDER BY 
    categoria;

-- Comparação de valores por tipo de gasto

SELECT 
    tipo_de_gasto, 
    SUM(valor) AS total_valor
FROM 
    data_out
GROUP BY 
    tipo_de_gasto
ORDER BY 
    total_valor DESC;

SELECT 
    categoria, 
    SUM(valor) AS total_valor, 
    ROUND(SUM(valor) * 100.0 / (SELECT SUM(valor) FROM data_out), 2) AS porcentagem
FROM 
    data_out
GROUP BY 
    categoria
ORDER BY 
    total_valor DESC;
