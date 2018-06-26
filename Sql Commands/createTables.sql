CREATE TABLE tb_person (
	pes_id int IDENTITY(1,1) NOT NULL,
	pes_name varchar(200) NOT NULL,
	pes_email varchar(120) NOT NULL,
	pes_pwd varchar(256) NOT NULL,
	pes_dtRegister datetime default(GETDATE()),
	pes_active BIT NOT NULL default(1),

	PRIMARY KEY CLUSTERED (pes_id ASC)
);


CREATE TABLE tb_access_log (
	acc_id int IDENTITY(1,1) NOT NULL,
	pes_id int,
	acc_ip text not null,
	acc_machine_name text not null,
	acc_dtAccess datetime default(GETDATE()),

	PRIMARY KEY CLUSTERED (acc_id ASC),
	FOREIGN KEY (pes_id) REFERENCES tb_person(pes_id)
);

CREATE TABLE tb_type_lottery(
	tpj_id int IDENTITY(1,1) NOT NULL,
	tpj_name varchar(120) NOT NULL,
	tpj_tensmin INT NOT NULL,
	tpj_betmin DECIMAL(10,2) NOT NULL,
	tpj_hitmin INT NOT NULL,
	tpj_hitmax INT NOT NULL,

	PRIMARY KEY CLUSTERED (tpj_id ASC)
);

insert into tb_type_lottery (tpj_name,tpj_tensmin, tpj_betmin, tpj_hitmin, tpj_hitmax) values ('Mega Sena',6,3.50,4,6)
insert into tb_type_lottery (tpj_name,tpj_tensmin, tpj_betmin, tpj_hitmin, tpj_hitmax) values ('Loto Fácil',15,2.00,11,16)

CREATE TABLE tb_lottery(
	lot_id int IDENTITY(1,1) NOT NULL,
	lot_concurse INT NOT NULL,
	lot_dtConcurse DATETIME NOT NULL,
	lot_game varchar(200) NOT NULL,
	lot_hit15 INT NOT NULL DEFAULT(0),
	lot_hit14 INT NOT NULL DEFAULT(0),
	lot_hit13 INT NOT NULL DEFAULT(0),
	lot_hit12 INT NOT NULL DEFAULT(0),
	lot_hit11 INT NOT NULL DEFAULT(0),
	lot_shared15 DECIMAL(10,2) NOT NULL DEFAULT(0),
	lot_shared14 DECIMAL(10,2) NOT NULL DEFAULT(0),
	lot_shared13 DECIMAL(10,2) NOT NULL DEFAULT(0),
	lot_shared12 DECIMAL(10,2) NOT NULL DEFAULT(0),
	lot_shared11 DECIMAL(10,2) NOT NULL DEFAULT(0),
	lot_dtNextConcurse DATETIME NOT NULL,
	tpj_id INT,

	PRIMARY KEY CLUSTERED (lot_id ASC),
	FOREIGN KEY (tpj_id) REFERENCES tb_type_lottery(tpj_id)
);

CREATE TABLE tb_person_lottery(
	pl_id int IDENTITY(1,1) NOT NULL,
	lot_id int, 
	pes_id int,
	pl_concurse INT NOT NULL,
	pl_game varchar(200) NOT NULL,
	pl_hits INT NOT NULL DEFAULT(0),
	pl_ticket_amount DECIMAL(10,2) NOT NULL DEFAULT(0),
	pl_scheduled_game DATETIME NULL, /*Caso o jogo esteja agendado para ser verificado em um dia específico*/
	pl_game_checked DATETIME NULL,
	pl_game_register datetime not null DEFAULT(GETDATE()),

	PRIMARY KEY CLUSTERED (pl_id ASC),
	FOREIGN KEY (lot_id) REFERENCES tb_lottery(lot_id),
	FOREIGN KEY (pes_id) REFERENCES tb_person(pes_id)
);

/*FAZER UMA TABELA DE LOG DE VERIFICAÇÃO*/

CREATE TABLE tb_email_sent_log(
	ema_id int IDENTITY(1,1) NOT NULL,
	id_person_who_sent INT NOT NULL DEFAULT(0),
	pes_id INT NOT NULL DEFAULT(0),
	ema_person_who_received_email text null, 
	ema_bcc text NULL,
	ema_cc text NULL,
	ema_dtSent DATETIME NOT NULL DEFAULT(GETDATE()),
	ema_subject text NULL,
	ema_message text NULL,
	ema_ticket_amount DECIMAL(10,2) NOT NULL DEFAULT(0),
	lot_concurse INT NOT NULL,
	ema_success BIT NOT NULL DEFAULT(0),
	ema_manually BIT NOT NULL DEFAULT(0),

	PRIMARY KEY CLUSTERED (ema_id ASC),
	FOREIGN KEY (pes_id) REFERENCES tb_person(pes_id)
);

CREATE TABLE tb_configuration(
	conf_id int IDENTITY(1,1) NOT NULL,
	conf_calculate_tens_without_success BIT NOT NULL DEFAULT(0),
	conf_send_email_manually BIT NOT NULL DEFAULT(0),
	conf_send_email_automatically BIT NOT NULL DEFAULT(0),
	conf_check_game_online BIT NOT NULL DEFAULT(0),
	conf_min_amount_to_send_email DECIMAL(10,2) NOT NULL DEFAULT(0),
	pes_id int not null DEFAULT(0)

	PRIMARY KEY CLUSTERED (conf_id ASC)
);

INSERT INTO tb_configuration  (conf_calculate_tens_without_success, conf_send_email_manually,
							  conf_send_email_automatically, conf_check_game_online, 
							  conf_min_amount_to_send_email)
							  VALUES (0,0,0,0,0, 1)

/*
Tabela de Permissão
1 - Admin
2 - Usuario
*/
CREATE TABLE tb_permition(
	per_id int IDENTITY(1,1) NOT NULL,
	per_name varchar(200) NOT NULL,

	PRIMARY KEY CLUSTERED (per_id ASC)
);

insert into tb_permition(per_name) values ('usuario')
insert into tb_permition(per_name) values ('administrador')

/*
Nivel de permissão
Exemplo:
	id(da propriatabela) - 1 (admin) - conf_id (Enviar email automatico)
*/
CREATE TABLE tb_level_permition(
	lvl_id int IDENTITY(1,1) NOT NULL,
	perm_id int,
	conf_id int
	
	PRIMARY KEY CLUSTERED (lvl_id ASC),
	FOREIGN KEY (perm_id) REFERENCES tb_level(perm_id),
	FOREIGN KEY (conf_id) REFERENCES tb_configuration(conf_id)
);

insert into tb_level_permition (per_id,conf_id) VALUES (2, 1)
/*
   1 pes_id - 1 lvl_id (Pessoa que tem essa permissão)
   1 pes_id - 2 lvl_id (Pessoa que tem essa permissão)
*/
CREATE TABLE tb_person_level_permition(
	pes_id int,
	lvl_id int,
	
	FOREIGN KEY (pes_id) REFERENCES tb_person(pes_id),
	FOREIGN KEY (lvl_id) REFERENCES tb_level_permition(lvl_id)
);



