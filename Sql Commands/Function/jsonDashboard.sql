USE [dbloteria]
GO
/****** Object:  UserDefinedFunction [dbo].[jsonDashboard]    Script Date: 24/06/2018 11:27:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER FUNCTION [dbo].[jsonDashboard](@concurseID INT)  
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
	--DECLARE @shared15Anterior INT = 0;

				SELECT TOP 1 
				 lot_concurse, 
				 FORMAT(lot_dtConcurse, 'dd/MM/yyyy') as lot_dtConcurse,
				 --FORMAT(lot_dtConcurse, 'dd/MM/yyyy hh:mm:ss'),
				 dbo.INITCAP(FORMAT(lot_dtConcurse, 'D')) as 'data_extenso',
				 lot_game,
				 lot_hit15, lot_shared15, 
				 (SELECT TOP 1 cast((ISNULL(lot_shared15, 100)*100/ISNULL((SELECT TOP 1  CASE WHEN lot_shared15 = 0 THEN 100 ELSE lot_shared15 END   from tb_lottery WHERE lot_concurse = (SELECT TOP 1 lot_concurse -1 from tb_lottery order by lot_concurse desc )	order by lot_concurse desc), 100) - 100) as decimal(10,2)) from tb_lottery order by lot_concurse desc)  as '_15Porcentagem',
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