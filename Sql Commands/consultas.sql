--REINICIA O VALOR IDENTITY DA CHAVE PRIMARIA
--DBCC CHECKIDENT('tb_lottery', RESEED, 0)

--SET STATISTICS IO ON
--SET STATISTICS TIME ON

/*Verifica se tem jogos repetidos*/
select lot_game, count(lot_game) as jogo
from tb_lottery
where
 tpj_id = 2
 group by lot_game


 select * from tb_person

 /*Total dos jogos*/
 select sum(lot_shared15) as '15 Pontos', sum(lot_shared14) as '14 Pontos',
		 sum(lot_shared13) as '13 Pontos', sum(lot_shared12) as '12 Pontos', sum(lot_shared11) as '11 Pontos'
		from tb_lottery where tpj_id =2

 select sum(lot_shared11) from tb_lottery where tpj_id =2

/*Coloca em ordem do maior pagamento já realizado até o menor*/
select lot_concurse, lot_game, lot_dtConcurse,lot_hit15, lot_shared15
 from tb_lottery 
where
 tpj_id = 2
 and
 lot_hit15 > 0
 order by lot_shared15 desc

 

 /*Verifica quantos jogos sem nenhum ganhador com 15 pontos*/
 select count(lot_concurse) - (select count(lot_concurse)
								 from tb_lottery 
								where
								 tpj_id = 2
								 and
								 lot_hit15 > 0) as 'Jogos sem ganhadores (15 Pontos)'
 from tb_lottery
 where tpj_id = 2


 
select pes_name, pl.pl_concurse, pl_hits
 from tb_person_lottery pl
inner join tb_person pes on pl.pes_id = pes.pes_id
inner join tb_lottery lot on pl.lot_id = lot.lot_id






--INSERT INTO tb_person_lottery (lot_id, pes_id, lot_concurse, lot_game) VALUES (372, 2, 1671, '01-02-03-05-08-09-10-11-14-15-16-19-23-24-25')
--INSERT INTO tb_person_lottery (lot_id, pes_id, lot_concurse, lot_game) VALUES (372, 2, 1671, '01-02-03-05-08-09-10-11-14-15-17-19-22-23-25')
--INSERT INTO tb_person_lottery (lot_id, pes_id, lot_concurse, lot_game) VALUES (372, 2, 1671, '01-02-03-05-06-08-09-10-12-15-19-21-22-23-25')

--1 diego
--2 bruna


--select * from tb_person_lottery

--update tb_person_lottery set lot_id = 351, lot_concurse = 1650
--where pes_id = 2 and pl_id in (1,2,3)


--update tb_person_lottery set pl_hits = 9, pl_game_checked = cast('17/04/2018' as datetime)
--where pes_id = 2 and pl_id in (1)



--update tb_person_lottery set pl_hits = 10, pl_game_checked = cast('17/04/2018' as datetime)
--where pes_id = 2 and pl_id in (2)



--update tb_person_lottery set pl_hits = 8, pl_game_checked = cast('17/04/2018' as datetime)
--where pes_id = 2 and pl_id in (3)




select pes.pes_name, count(lg.ema_id) as 'Quantidade de Email', 
case when lg.ema_manually = 0 THEN 'Envio Automático' ELSE 'Envio Manual' END as 'Envio' 
from tb_email_sent_log lg
LEFT join tb_person pes on lg.pes_id = pes.pes_id
--where 
--lg.lot_concurse = 1675
--pes.pes_id = 1
group by lg.ema_id, pes.pes_name, lg.ema_manually