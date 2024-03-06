DROP TABLE IF EXISTS public.ofac_cons_add;
CREATE TABLE IF NOT EXISTS public.ofac_cons_add(
	ent_num integer,
	add_num integer,
	address varchar(750) COLLATE pg_catalog."default",
	complete_address varchar(116) COLLATE pg_catalog."default",
	country varchar(250) COLLATE pg_catalog."default",
	add_remarks varchar(200) COLLATE pg_catalog."default"
);

DROP TABLE IF EXISTS public.ofac_cons_alt;
CREATE TABLE IF NOT EXISTS public.ofac_cons_alt (
	ent_num integer,
	alt_num integer,
	alt_type varchar(8) COLLATE pg_catalog."default",
	alt_name varchar(350) COLLATE pg_catalog."default",
	alt_remarks varchar(200) COLLATE pg_catalog."default"
);

DROP TABLE IF EXISTS public.ofac_cons_prim;
CREATE TABLE IF NOT EXISTS public.ofac_cons_prim (
	ent_num integer,
	sdn_name varchar(350) COLLATE pg_catalog."default",
	sdn_type varchar(12) COLLATE pg_catalog."default",
	program varchar(200) COLLATE pg_catalog."default",
	title varchar(200) COLLATE pg_catalog."default",
	call_sign varchar(8) COLLATE pg_catalog."default",
	vess_type varchar(25) COLLATE pg_catalog."default",
	tonnage varchar(14) COLLATE pg_catalog."default",
	grt varchar(8) COLLATE pg_catalog."default",
	vess_flag varchar(40) COLLATE pg_catalog."default",
	vess_owner varchar(150) COLLATE pg_catalog."default",
	remarks varchar(1000) COLLATE pg_catalog."default"
);