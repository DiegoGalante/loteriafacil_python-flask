--IF OBJECT_ID (N'Sales.ufn_SalesByStore', N'IF') IS NOT NULL  
    --DROP FUNCTION jsonDashboard;  
--GO  
ALTER FUNCTION jsonDashboard(@concurseID INT)  
RETURNS TABLE  
AS  
RETURN   
(  
	--IF ISNULL(@concurseID,0) > 0
	-- BEGIN
	--		SELECT TOP 1 
	--		 lot_concurse, 
	--		 FORMAT(lot_dtConcurse, 'dd/MM/yyyy') as lot_dtConcurse,
	--		 --FORMAT(lot_dtConcurse, 'dd/MM/yyyy hh:mm:ss'),
	--		 dbo.INITCAP(FORMAT(lot_dtConcurse, 'D')) as 'data_extenso',
	--		 lot_game,
	--		 lot_hit15, lot_shared15, 
	--		 (SELECT TOP 1 cast((lot_shared15*100/(SELECT TOP 1  lot_shared15 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_15Porcentagem',
	--		 lot_hit14, lot_shared14,  
	--		 (SELECT TOP 1 cast((lot_shared14*100/(SELECT TOP 1  lot_shared14 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_14Porcentagem',
	--		 lot_hit13, lot_shared13,  
	--		 (SELECT TOP 1 cast((lot_shared13*100/(SELECT TOP 1  lot_shared13 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_13Porcentagem',
	--		 lot_hit12, lot_shared12,  
	--		 (SELECT TOP 1 cast((lot_shared12*100/(SELECT TOP 1  lot_shared12 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_12Porcentagem',
	--		 lot_hit11, lot_shared11,
	--		 (SELECT TOP 1 cast((lot_shared11*100/(SELECT TOP 1  lot_shared11 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_11Porcentagem'
	--	FROM tb_lottery
	--		WHERE
	--			tpj_id = 2 and lot_concurse = @concurseID
	--	ORDER BY 1 DESC
	--END
	--ELSE
	-- BEGIN

				SELECT TOP 1 
				 lot_concurse, 
				 FORMAT(lot_dtConcurse, 'dd/MM/yyyy') as lot_dtConcurse,
				 --FORMAT(lot_dtConcurse, 'dd/MM/yyyy hh:mm:ss'),
				 dbo.INITCAP(FORMAT(lot_dtConcurse, 'D')) as 'data_extenso',
				 lot_game,
				 lot_hit15, lot_shared15, 
				 (SELECT TOP 1 cast((lot_shared15*100/(SELECT TOP 1  lot_shared15 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_15Porcentagem',
				 lot_hit14, lot_shared14,  
				 (SELECT TOP 1 cast((lot_shared14*100/(SELECT TOP 1  lot_shared14 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_14Porcentagem',
				 lot_hit13, lot_shared13,  
				 (SELECT TOP 1 cast((lot_shared13*100/(SELECT TOP 1  lot_shared13 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_13Porcentagem',
				 lot_hit12, lot_shared12,  
				 (SELECT TOP 1 cast((lot_shared12*100/(SELECT TOP 1  lot_shared12 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_12Porcentagem',
				 lot_hit11, lot_shared11,
				 (SELECT TOP 1 cast((lot_shared11*100/(SELECT TOP 1  lot_shared11 from tb_lottery 	WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_11Porcentagem'
				FROM tb_lottery
				WHERE
					tpj_id = 2
					and lot_concurse = @concurseID
				ORDER BY 1 DESC
--		END
--END
)  

ALTER FUNCTION jogoPessoa (@concurseID INT)  
RETURNS TABLE  
AS  
RETURN   
(  

	SELECT  pl.pl_id, pl.pl_concurse, pes.pes_name, pl.pl_game, pl.pl_hits, pl.pl_ticket_amount as pl_ticket_amount
	 FROM tb_person_lottery pl
	inner join tb_lottery lot on pl.lot_id = lot.lot_id
	inner join tb_person pes on pl.pes_id = pes.pes_id
	WHERE lot.tpj_id = 2 
	and lot_concurse = @concurseID
	
);

--DECLARE @concursoAtual INT = (SELECT TOP 1  lot_concurse from tb_lottery order by 1 desc )
--print @concursoAtual

--DECLARE @concursoBusca INT = 1650

SELECT top 1 cast(lot_shared14 as decimal(10,2))*100/ 
	(CASE WHEN (SELECT top 1 cast(lot_shared14 as decimal(10,2)) from tb_lottery where lot_concurse = 1650) = 0 THEN 1 ELSE 'TESTE' END ) - 100
 from tb_lottery where lot_concurse = 1672 


 select (898459.93 * 100 / 605656.21) - 100

 --por não conseguir dividir por 0, então jogo o valor original e não retiro o 100
 select (898459.93 * 100 / 898459.93)


/*RECUPERA O VALOR do concurso atual*/
 DECLARE @lot_shared15Atual DECIMAL = (SELECT TOP 1 lot_shared15 from tb_lottery order by 1 desc)

 /*RECUPERA O VALOR do concurso que foi retornado*/
 DECLARE @lot_shared15Busca  DECIMAL = (SELECT TOP 1 CASE WHEN lot_shared15 = 0 THEN @lot_shared15Atual  ELSE lot_shared15 END from tb_lottery WHERE lot_concurse = 1650 order by 1 desc)
 print @lot_shared15Busca

 select CASE WHEN @lot_shared15Atual = @lot_shared15Busca THEN ((@lot_shared15Atual * 100 / @lot_shared15Busca) - 100) - 100 ELSE (@lot_shared15Atual * 100 / @lot_shared15Busca) - 100 END

--SELECT TOP 1 cast((lot_shared15*100/
--									(SELECT top 1  cast(lot_shared15 as decimal(10,2)) from tb_lottery where lot_concurse = @concursoAtual order by lot_concurse desc ) ) as decimal(10,2))
--from tb_lottery 
--where lot_concurse = @concursoBusca
--order by lot_concurse desc

DECLARE @numConcurso INT = 1642
select * from jsonDashboard(@numConcurso)

SET @numConcurso  = 1660
select * from jsonDashboard(@numConcurso)

SET @numConcurso  = 1670
select * from jsonDashboard(@numConcurso)

SET @numConcurso  = 1669
select * from jsonDashboard(@numConcurso)

SET @numConcurso  = 1671
select * from jsonDashboard(@numConcurso)

select * from jogoPessoa(@numConcurso) order by pl_hits desc

select top 100 lot_concurse from tb_lottery order by 1 desc


--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-04-05-08-09-10-11-14-16-17-19-22-23-25", hits:10, id:4, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:5, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-12-15-17-19-22-23-25", hits:10, id:6, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-06-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:7, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:8, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-07-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:9, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:10, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:11, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:12, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:13, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:14, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:13, id:15, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:16, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:17, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:18, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:19, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:14, id:20, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:21, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:22, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:23, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:24, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:15, id:25, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:26, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:27, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:28, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:29, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:30, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:40, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:41, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:42, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:43, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:44, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:13, id:45, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:46, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:47, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:48, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:49, name:"Diego Galante" })
--data.dados[0].personGame.push( {amount:0, concurse:1650, game: "01-02-03-05-08-09-10-11-14-15-17-19-22-23-25", hits:10, id:50, name:"Diego Galante" })


DECLARE @concurseAtual INT = 1;
DECLARE @nexConcurse INT = @concurseAtual+1;

DECLARE @maxConcurse INT = (SELECT TOP 1 lot_concurse from tb_lottery order by 1 desc)+1

WHILE @nexConcurse < @maxConcurse
BEGIN
	print concat('CONCURSO ATUAL: ',@concurseAtual)
	print concat('Proximo Concurso: ',@nexConcurse)

	--select (lot_dtConcurse + DATEDIFF(DAY, lot_dtConcurse, (select lot_dtConcurse  from tb_lottery where lot_concurse = @nexConcurse)))
	update lot set lot_dtNextConcurse = (lot_dtConcurse + DATEDIFF(DAY, lot_dtConcurse, (select lot_dtConcurse  from tb_lottery where lot_concurse = @nexConcurse)))
	from tb_lottery lot
	where lot_concurse = @concurseAtual

	 --select lot_id, lot_concurse, lot_dtConcurse, lot_dtConcurse + DATEDIFF(DAY, lot_dtConcurse, (select lot_dtConcurse  from tb_lottery where lot_concurse = @nexConcurse)) as dtNextConcurse
	 --,DATEDIFF(DAY, lot_dtConcurse, (select lot_dtConcurse  from tb_lottery where lot_concurse = @nexConcurse)) as 'date'  from tb_lottery where lot_concurse = @concurseAtual

	SET @concurseAtual += 1;
	SET @nexConcurse += 1;
END






