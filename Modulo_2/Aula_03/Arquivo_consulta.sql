CREATE DATABASE vendas_online;
use vendas_online;
CREATE TABLE produtos (
id_produto INT PRIMARY KEY,
nome VARCHAR(255),
categoria VARCHAR(100),
preco DECIMAL(10, 2),
estoque INT
);
-- DQL (Data Query Language) --
SELECT * FROM produtos;

SELECT nome, preco FROM produtos;

SELECT nome as nome_produto, preco as preço_produto FROM produtos WHERE preco < 1000;

SELECT nome, categoria FROM produtos WHERE categoria = 'Eletrônicos';