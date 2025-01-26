-- Table: public.data_in

-- DROP TABLE IF EXISTS public.data_in;

CREATE TABLE IF NOT EXISTS public.data_in
(
    id integer NOT NULL DEFAULT nextval('data_in_id_seq'::regclass),
    data date NOT NULL,
    origem text COLLATE pg_catalog."default",
    categoria text COLLATE pg_catalog."default",
    data_in text COLLATE pg_catalog."default",
    data_out text COLLATE pg_catalog."default",
    valor numeric(10,2),
    CONSTRAINT data_in_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.data_in
    OWNER to postgres;