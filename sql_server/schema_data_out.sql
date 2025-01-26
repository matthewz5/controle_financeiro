-- Table: public.data_out

-- DROP TABLE IF EXISTS public.data_out;

CREATE TABLE IF NOT EXISTS public.data_out
(
    id integer NOT NULL DEFAULT nextval('data_out_id_seq'::regclass),
    data date NOT NULL,
    hora time without time zone NOT NULL,
    categoria text COLLATE pg_catalog."default",
    tipo_de_gasto text COLLATE pg_catalog."default",
    fonte text COLLATE pg_catalog."default",
    sub_fonte text COLLATE pg_catalog."default",
    local text COLLATE pg_catalog."default",
    item text COLLATE pg_catalog."default",
    descricao_item text COLLATE pg_catalog."default",
    valor_unitario numeric(10,2),
    quantidade numeric(10,2),
    valor numeric(10,2),
    CONSTRAINT data_out_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.data_out
    OWNER to postgres;