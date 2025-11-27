SET GLOBAL local_infile = 1;
LOAD DATA LOCAL INFILE 'C:/Users/felix.thiago/Documents/BigDataSenacNI/Modulo_2/Aula_04/vendas_clientes.csv'
INTO TABLE vendas_online.produtos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS 
SET preco = REPLACE(@preco_var, '.',',');
