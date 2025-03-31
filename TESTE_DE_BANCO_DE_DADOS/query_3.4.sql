COPY public."1T2024" ("DATA", "REG_ANS", "CD_CONTA", "DESCRICA", "VL_SALDO", "VL_SALDO_FINAL")
FROM 'D:/1T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY public."2T2024" ("DATA", "REG_ANS", "CD_CONTA", "DESCRICA", "VL_SALDO", "VL_SALDO_FINAL")
FROM 'D:/2T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY public."3T2024" ("DATA", "REG_ANS", "CD_CONTA", "DESCRICA", "VL_SALDO", "VL_SALDO_FINAL")
FROM 'D:/3T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY public."4T2024" ("DATA", "REG_ANS", "CD_CONTA", "DESCRICA", "VL_SALDO", "VL_SALDO_FINAL")
FROM 'D:/4T2024.csv'
DELIMITER ';'
CSV HEADER;



COPY public.registro_ans ("registro_ans", "cnpj", "razao_social", "nome_fantasia", 
"modalidade", "logradouro", "numero", "complemento", "bairro", "cidade", "uf", "cep", 
"ddd", "telefone", "fax", "endereco_eletronico", "representante", "cargo_representante", 
"regiao_de_comercializacao", "data_registro_ans") 
FROM 'D:/operadoras_saude.csv' DELIMITER ';' CSV HEADER;



