CREATE TABLE IF NOT EXISTS public."4T2024"
(
    "DATA" character varying(255) COLLATE pg_catalog."default",
    "REG_ANS" integer,
    "CD_CONTA" integer,
    "DESCRICA" character varying COLLATE pg_catalog."default",
    "VL_SALDO" numeric,
    "VL_SALDO_FINAL" numeric
)

-------------------------------------------------------------------------


CREATE TABLE IF NOT EXISTS public."3T2024"
(
    "DATA" character varying(255) COLLATE pg_catalog."default",
    "REG_ANS" integer,
    "CD_CONTA" integer,
    "DESCRICA" character varying COLLATE pg_catalog."default",
    "VL_SALDO" numeric,
    "VL_SALDO_FINAL" numeric
)



CREATE TABLE IF NOT EXISTS public."2T2024"
(
    "DATA" character varying(255) COLLATE pg_catalog."default",
    "REG_ANS" integer,
    "CD_CONTA" integer,
    "DESCRICA" character varying COLLATE pg_catalog."default",
    "VL_SALDO" numeric,
    "VL_SALDO_FINAL" numeric
)



CREATE TABLE IF NOT EXISTS public."1T2024"
(
    "DATA" character varying(255) COLLATE pg_catalog."default",
    "REG_ANS" integer,
    "CD_CONTA" integer,
    "DESCRICA" character varying COLLATE pg_catalog."default",
    "VL_SALDO" numeric,
    "VL_SALDO_FINAL" numeric
)



CREATE TABLE IF NOT EXISTS public.registro_ans
(
    registro_ans integer NOT NULL,
    cnpj character varying(20) COLLATE pg_catalog."default",
    razao_social character varying(255) COLLATE pg_catalog."default",
    nome_fantasia character varying(255) COLLATE pg_catalog."default",
    modalidade character varying(100) COLLATE pg_catalog."default",
    logradouro character varying(255) COLLATE pg_catalog."default",
    numero text COLLATE pg_catalog."default",
    complemento character varying(255) COLLATE pg_catalog."default",
    bairro character varying(255) COLLATE pg_catalog."default",
    cidade character varying(255) COLLATE pg_catalog."default",
    uf character(2) COLLATE pg_catalog."default",
    cep character varying(10) COLLATE pg_catalog."default",
    ddd character(2) COLLATE pg_catalog."default",
    telefone character varying(20) COLLATE pg_catalog."default",
    fax character varying(20) COLLATE pg_catalog."default",
    endereco_eletronico character varying(255) COLLATE pg_catalog."default",
    representante character varying(255) COLLATE pg_catalog."default",
    cargo_representante character varying(255) COLLATE pg_catalog."default",
    regiao_de_comercializacao integer,
    data_registro_ans date,
    CONSTRAINT registro_ans_pkey PRIMARY KEY (registro_ans)
)