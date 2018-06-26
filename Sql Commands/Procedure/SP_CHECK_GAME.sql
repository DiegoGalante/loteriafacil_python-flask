USE [dbloteria]
GO
/****** Object:  StoredProcedure [dbo].[SP_CHECK_GAME]    Script Date: 25/06/2018 16:04:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[SP_CHECK_GAME](
	@lot_concurse INT,
	@tpj_id INT = 2,
	@pes_id INT = 0
) --FIM PARAMETROS
AS
BEGIN
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

-- exec SP_CHECK_GAME 1679, 2

--INSERT INTO tb_person_lottery (pes_id, pl_concurse, pl_game) values (1, 1675,'01-02-03-05-08-09-10-11-14-15-16-19-23-24-25' )
--	INSERT INTO tb_person_lottery (pes_id, pl_concurse, pl_game) values (1, 1675,'01-02-03-05-08-09-10-11-14-15-17-19-22-23-25' )
--	INSERT INTO tb_person_lottery (pes_id, pl_concurse, pl_game) values (1, 1675,'01-02-03-05-06-08-09-10-12-15-19-21-22-23-25' )

	--UPDATE tb_person_lottery
	--		SET 
	--			lot_id = null,
	--			pl_hits = 0,
	--			pl_game_checked = null
	--		WHERE
	--		pl_concurse = 1679

	--delete from tb_lottery where lot_concurse = 1679
	

	-- DECLARE @game varchar(100) = (SELECT TOP 1 lot_game from tb_lottery  where lot_concurse = @lot_concurse and tpj_id = @tpj_id order by 1 desc);
	DECLARE @lot_game varchar(100);
	DECLARE @lot_id INT;
	DECLARE @lot_shared15 DECIMAL(10,2);
	DECLARE @lot_shared14 DECIMAL(10,2);
	DECLARE @lot_shared13 DECIMAL(10,2);
	DECLARE @lot_shared12 DECIMAL(10,2);
	DECLARE @lot_shared11 DECIMAL(10,2);
	
	SELECT TOP 1 @lot_id = lot_id, 
	@lot_game = lot_game, 
	@lot_shared15 = lot_shared15, 
	@lot_shared14 = lot_shared14, 
	@lot_shared13 = lot_shared13, 
	@lot_shared12 = lot_shared12, 
	@lot_shared11 = lot_shared11
	FROM tb_lottery 
	where lot_concurse = @lot_concurse
	and tpj_id = @tpj_id

	DECLARE @hit_pessoa INT = 0;

	DECLARE @gamePessoas varchar(100)
	DECLARE @pl_id INT
	DECLARE @ticket_amount DECIMAL(10,2)

	print('Declara o cursor: db_cursorPessoas');
	IF @pes_id = 0
	BEGIN 
	DECLARE db_cursorPessoas CURSOR FOR
	SELECT  pl.pl_id, pl.pl_game
			FROM tb_person_lottery pl
			WHERE
			pl.pl_concurse = @lot_concurse 
			and
			ISNULL(pl.pl_game_checked, null) is null 
	END
	ELSE
	BEGIN
	DECLARE db_cursorPessoas CURSOR FOR
	SELECT  pl.pl_id, pl.pl_game
			FROM tb_person_lottery pl
			WHERE
			pl.pl_concurse = @lot_concurse 
			and
			pl.pes_id = @pes_id
			and
			ISNULL(pl.pl_game_checked, null) is null 
	END


	print('Abre o cursor: db_cursorPessoas');
	open db_cursorPessoas
	FETCH NEXT FROM db_cursorPessoas INTO @pl_id, @gamePessoas
	
	print('Inicia o cursor: db_cursorPessoas');
	WHILE @@FETCH_STATUS = 0  
	--INICIA O db_cursor
	BEGIN
		SET @hit_pessoa =0;

		select value into #gameLoteria FROM string_split(@lot_game, '-')  WHERE 	RTRIM(LTRIM(value)) <> ''
		ALTER TABLE #gameLoteria
		ADD lot_game int NULL DEFAULT(NULL);

		ALTER TABLE #gameLoteria
		ADD pl_id int NULL DEFAULT(null);

		UPDATE #gameLoteria set lot_game = @lot_concurse;
		UPDATE #gameLoteria set pl_id = @pl_id;

		SELECT value into #gamePessoa FROM string_split(@gamePessoas, '-')  WHERE 	RTRIM(LTRIM(value)) <> ''
		ALTER TABLE #gamePessoa
		ADD lot_game int NULL DEFAULT(null);

		ALTER TABLE #gamePessoa
		ADD pl_id int NULL DEFAULT(null);

		UPDATE #gamePessoa set pl_id = @pl_id;
		UPDATE #gamePessoa set lot_game = @lot_concurse;

		--select * from #gameLoteria
		--select * from #gamePessoa

		SET @hit_pessoa = (select count(pes.value) as cont from #gamePessoa pes
		INNER JOIN #gameLoteria lot on pes.lot_game = lot.lot_game
		WHERE cast(pes.value as int) = cast(lot.value as int)
		and pes.pl_id = lot.pl_id
		and pes.lot_game = lot.lot_game)
		--select count(pes.value) as cont from #gamePessoa pes
		--INNER JOIN #gameLoteria lot on pes.lot_game = lot.lot_game
		----INNER JOIN tb_person_lottery pl on pes.pes_id = pl.pes_id
		--WHERE cast(pes.value as int) = cast(lot.value as int)
		--and pes.pl_id = lot.pl_id

		print(concat('HIT_PESSOA: ', @hit_pessoa));
						
		drop table #gameLoteria
		drop table #gamePessoa

		IF @hit_pessoa = 15
		BEGIN
			SET @ticket_amount = @lot_shared15;
		END
		ELSE IF @hit_pessoa = 14
		BEGIN
			SET @ticket_amount = @lot_shared14;
		END
		ELSE IF @hit_pessoa = 13
		BEGIN
			SET @ticket_amount = @lot_shared13;
		END
		ELSE IF @hit_pessoa = 12
		BEGIN
			SET @ticket_amount = @lot_shared12;
		END
		ELSE IF @hit_pessoa = 11
		BEGIN
			SET @ticket_amount = @lot_shared11;
		END
		ELSE IF @hit_pessoa <= 10
		BEGIN
			SET @ticket_amount = 0;
		END
				
		print(CONCAT('PL_ID: ', @pl_id))
		UPDATE tb_person_lottery 
			SET pl_hits = @hit_pessoa, lot_id = @lot_id, pl_ticket_amount = ISNULL(@ticket_amount, 0), pl_game_checked = GETDATE()
		WHERE pl_id = @pl_id and pl_concurse = @lot_concurse

	print('Seta o próximo loop do cursor: db_cursorPessoas');
	FETCH NEXT FROM db_cursorPessoas INTO  @pl_id, @gamePessoas
	END 
	
	print('Fecha o cursor: db_cursorPessoas');
	CLOSE db_cursorPessoas  
	print('Desaloca o cursor: db_cursorPessoas');
	DEALLOCATE db_cursorPessoas 

	IF @pes_id = 0
	BEGIN 
		SELECT 
		count(*)
		--pl_id, lot_id, pes_id, pl_concurse, pl_game, pl_hits, pl_ticket_amount, pl_scheduled_game, pl_game_checked 
		FROM tb_person_lottery
		WHERE pl_concurse = @lot_concurse
		and ISNULL(pl_game_checked, null) is null
		--ORDER BY pl_hits DESC
	END
	ELSE
	BEGIN
		SELECT 
		count(*)
		--pl_id, lot_id, pes_id, pl_concurse, pl_game, pl_hits, pl_ticket_amount, pl_scheduled_game, pl_game_checked 
		FROM tb_person_lottery
		WHERE pl_concurse = @lot_concurse
		and ISNULL(pl_game_checked, null) is null
		and pes_id = @pes_id
		--ORDER BY pl_hits DESC
	END
	
--SQL Server Cursor Components
--Based on the example above, cursors include these components:

--DECLARE statements - Declare variables used in the code block
--SET\SELECT statements - Initialize the variables to a specific value
--DECLARE CURSOR statement - Populate the cursor with values that will be evaluated
--NOTE - There are an equal number of variables in the DECLARE CURSOR FOR statement as there are in the SELECT statement.  This could be 1 or many variables and associated columns.
--OPEN statement - Open the cursor to begin data processing
--FETCH NEXT statements - Assign the specific values from the cursor to the variables
--NOTE - This logic is used for the initial population before the WHILE statement and then again during each loop in the process as a portion of the WHILE statement
--WHILE statement - Condition to begin and continue data processing
--BEGIN...END statement - Start and end of the code block
--NOTE - Based on the data processing multiple BEGIN...END statements can be used
--Data processing - In this example, this logic is to backup a database to a specific path and file name, but this could be just about any DML or administrative logic
--CLOSE statement - Releases the current data and associated locks, but permits the cursor to be re-opened
--DEALLOCATE statement - Destroys the cursor

END