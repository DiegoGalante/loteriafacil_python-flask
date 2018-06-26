USE [dbloteria]
GO
/****** Object:  StoredProcedure [dbo].[SP_SAVE_LOG_EMAIL]    Script Date: 24/06/2018 11:26:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[SP_SAVE_LOG_EMAIL](
	@ema_id INT, 
	@id_person_who_sent INT,
	@id_person_who_received INT, 
	@ema_person_who_received_email varchar(MAX),
	@ema_bcc varchar(MAX),
	@ema_cc varchar(MAX),
	@ema_dtSent varchar(10),
	@ema_subject varchar(max),
	@ema_message text,
	@ema_ticket_amount decimal,
	@lot_concurse INT,
	@ema_success BIT,
	@ema_manually BIT
) --FIM PARAMETROS
AS
BEGIN
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

-- exec SP_CHECK_GAME 1673, 2
	print('Declarando variável da data')
	DECLARE @dtSent DATETIME;
	IF @ema_dtSent <> ''
	BEGIN
	 SET @dtSent = cast(@ema_dtSent as datetime2)
	END
	ELSE
	BEGIN 
		SET @dtSent = GETDATE()	
	END

	IF @ema_id = 0
	BEGIN
		print('Inserindo na tabela tb_email_sent')
		INSERT INTO tb_email_sent_log (id_person_who_sent, pes_id, ema_person_who_received_email, ema_bcc, ema_cc, ema_dtSent, ema_subject, ema_message, ema_ticket_amount, lot_concurse, ema_success, ema_manually)
		VALUES (
			@id_person_who_sent,
			@id_person_who_received,
			@ema_person_who_received_email,
			@ema_bcc,
			@ema_cc,
			@dtSent,
			@ema_subject,
			@ema_message,
			@ema_ticket_amount,
			@lot_concurse,
			@ema_success,
			@ema_manually
		)
	END
	--ELSE
	--BEGIN
	--	UPDATE tb_email_sent SET
	--		id_person_who_sent
	--	WHERE ema_id = @ema_id
	--END
	
	print('Fim da Procedure')
END