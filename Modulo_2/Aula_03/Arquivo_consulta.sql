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

-- Aula 04 --

CREATE TABLE clientes ( 
    id_cliente INT PRIMARY KEY, 
    nome VARCHAR(255), 
    email VARCHAR(255) 
);

CREATE TABLE pedidos ( 
    id_pedido INT PRIMARY KEY, 
	id_cliente INT,
    data_pedido DATE, 
    valor_total DECIMAL(10, 2),  
    id_produto INT, 
    quantidade INT
); 

ALTER TABLE pedidos 
ADD CONSTRAINT fk_pedidos_clientes 
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos 
ADD CONSTRAINT fk_pedidos_produtos 
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);