USE [dbloteria]
GO
/****** Object:  UserDefinedFunction [dbo].[jogoPessoa]    Script Date: 25/06/2018 22:16:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER FUNCTION [dbo].[jogoPessoa] (@concurseID INT)  
RETURNS TABLE  
AS  
RETURN   
(  

	SELECT  pl.pl_id, pl.pl_concurse, pes.pes_name, pl.pl_game, pl.pl_hits, pl.pl_ticket_amount as pl_ticket_amount, pes.pes_id
	 FROM tb_person_lottery pl
	inner join tb_lottery lot on pl.lot_id = lot.lot_id
	inner join tb_person pes on pl.pes_id = pes.pes_id
	WHERE lot.tpj_id = 2 
	and lot_concurse = @concurseID
	--and pes.pes_id = 1
	group by pl.pl_id, pl.pl_concurse, pes.pes_id, pes.pes_name, pl.pl_game, pl.pl_hits, pl.pl_ticket_amount 
	
);