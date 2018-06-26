
DECLARE @pes_id INT = 1;
DECLARE @numConcurso INT = 1679;

DECLARE @11Fixa nvarchar(50) ='01-02-03-05-06-08-09-10-11-16-17-'

DECLARE @g1 nvarchar(5) = '18-21';
DECLARE @g2 nvarchar(5) ='20-19';
DECLARE @g3 nvarchar(5) ='22-15';
DECLARE @g4 nvarchar(5) ='23-24';
DECLARE @g5 nvarchar(5) ='07-04';
DECLARE @g6 nvarchar(5) ='12-25';
DECLARE @g7 nvarchar(5) ='13-14';

insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso, CONCAT(@11Fixa, @g1, '-', @g2))
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso, CONCAT(@11Fixa, @g1, '-', @g3))
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso, CONCAT(@11Fixa, @g1, '-', @g4))
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso, CONCAT(@11Fixa, @g1, '-', @g5))
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso, CONCAT(@11Fixa, @g1, '-', @g6))
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso, CONCAT(@11Fixa, @g1, '-', @g7))  


insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g2, '-', @g3) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g2, '-', @g4) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g2, '-', @g5) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g2, '-', @g6) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g2, '-', @g7) )

insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g3, '-', @g4) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g3, '-', @g5) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g3, '-', @g6) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g3, '-', @g7) )

insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g4, '-', @g5) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g4, '-', @g6) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g4, '-', @g7) )

insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g5, '-', @g6) )
insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g5, '-', @g7) )

insert into tb_person_lottery (pes_id, pl_concurse, pl_game) values (@pes_id, @numConcurso,CONCAT(@11Fixa, @g6, '-', @g7) )

select * from tb_person_lottery where pl_concurse = @numConcurso