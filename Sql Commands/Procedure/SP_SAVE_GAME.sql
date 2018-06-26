USE [dbloteria]
GO
/****** Object:  StoredProcedure [dbo].[SP_SAVE_GAME]    Script Date: 25/06/2018 16:05:08 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[SP_SAVE_GAME](
	@lot_id INT, @lot_concurse INT, @lot_dtConcurse nvarchar(10), @lot_game varchar(50), 
	@lot_hit15 INT, @lot_hit14 INT, @lot_hit13 INT, @lot_hit12 INT, @lot_hit11 INT,
	@lot_shared15 DECIMAL, @lot_shared14 DECIMAL, @lot_shared13 DECIMAL, @lot_shared12 DECIMAL, @lot_shared11 DECIMAL,
	@lot_dtNextConcurse nvarchar(10),
	@tpj_id INT
) --FIM PARAMETROS
AS
BEGIN
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

	-- EXEC SP_SAVE_GAME 0, 1675, '2018-06-13', '01-02-03-05-07-08-09-12-14-19-20-21-22-23-25', 1, 495, 18009, 219899, 1092382, 1453985.03, 1291.13, 20.0, 8.0, 4.0, 2	
	DECLARE @contJogo INT = 0;
	--Formato da data 2018-05-31 // yyyy/mm/dd
	DECLARE @dataJogo DATETIME = cast(@lot_dtConcurse as datetime2)
	DECLARE @dataProximoJogo DATETIME = cast(@lot_dtNextConcurse as datetime2)

	--IF @lot_id > 0 
	--BEGIN
	--	SET @contJogo = (select COUNT(lot_id) from tb_lottery WITH(NOLOCK)  where lot_id = @lot_id);
	--END

	--IF @contJogo = 0
	--BEGIN
		INSERT INTO tb_lottery
		(lot_concurse, lot_dtConcurse, lot_game, lot_hit15, lot_hit14, lot_hit13, lot_hit12, lot_hit11, lot_shared15, lot_shared14, lot_shared13, lot_shared12, lot_shared11 ,tpj_id, lot_dtNextConcurse)
		VALUES
		(@lot_concurse, @dataJogo, @lot_game, @lot_hit15,  @lot_hit14,  @lot_hit13,  @lot_hit12,  @lot_hit11, @lot_shared15,  @lot_shared14,  @lot_shared13,  @lot_shared12,  @lot_shared11, @tpj_id, @dataProximoJogo);
	--END
	--ELSE 
	--BEGIN
	--	UPDATE tb_lottery 
	--	SET lot_concurse = @lot_concurse, lot_dtConcurse = @dataJogo, lot_game=@lot_game, lot_hit15=@lot_hit15, lot_hit14=@lot_hit14, lot_hit13=@lot_hit13, lot_hit12=@lot_hit12, lot_hit11=@lot_hit11, lot_shared15=@lot_shared15, lot_shared14=@lot_shared14, lot_shared13=@lot_shared13, lot_shared12=@lot_shared12, lot_shared11=@lot_shared11, tpj_id=@tpj_id
	--	WHERE lot_id = @lot_id;
	--END


	--print('EXECUTA procedure de checar os jogos')
	--EXEC SP_CHECK_GAME @lot_concurse, @tpj_id


END

