from app import db
from app.models.tables import Lottery
from flask import jsonify, json

from app.controllers.jsonencoder import GenericJsonEncoder

from datetime import *
from decimal import Decimal

def RecuperaJogoSistema(tipoJogo, dtInicio, dtFim=None):
    pass


def RecuperaUltimoJogo(to_json=False):
    loteria = Lottery(None, None, None, None, None, None, None,
                      None, None, None, None, None, None, None, None, None)
    loterias = ''

    tipoJogo = 2
    sqlCommand = """
                    select top 1 
                    lot_id, lot_concurse, lot_dtConcurse, lot_game, 
                    lot_hit15, lot_hit14, lot_hit13, lot_hit12, lot_hit11,
                    lot_shared15, lot_shared14, lot_shared13, lot_shared12, lot_shared11, lot_dtNextConcurse, tpj_id
                    from tb_lottery where tpj_id = {0} order by lot_id desc
                 """.format(tipoJogo)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand)
    rows = result.fetchall()
    connection.close()
    if len(rows) == 1:
        for rowloterias in rows:
            loteria = Lottery(rowloterias[0], rowloterias[1], rowloterias[2], rowloterias[3], rowloterias[4], rowloterias[5], rowloterias[6],
                              rowloterias[7], rowloterias[8], rowloterias[9], rowloterias[10], rowloterias[11], rowloterias[12], rowloterias[13], rowloterias[14], rowloterias[15])
            # loterias.append(loteria.__str__())
            # loteria = []

        if to_json:
            return jsonify({'loteria': loteria.__str__()})
        else:
            return loteria


def RecuperaJogo(tipoJogo, numConcurso, to_json=False):
    loteria = Lottery(None, None, None, None, None, None, None,
                      None, None, None, None, None, None, None, None, None)
    loterias = []

    sqlCommand = """
                    select 
                    lot_id, lot_concurse, lot_dtConcurse, lot_game, 
                    lot_hit15, lot_hit14, lot_hit13, lot_hit12, lot_hit11,
                    lot_shared15, lot_shared14, lot_shared13, lot_shared12, lot_shared11, lot_dtNextConcurse, tpj_id
                    from tb_lottery where lot_concurse = {0} and tpj_id = {1}
                 """.format(numConcurso, tipoJogo)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand)
    rows = result.fetchall()
    connection.close()

    if len(rows) == 1:
        for rowloterias in rows:
            loteria = Lottery(rowloterias[0], rowloterias[1], rowloterias[2], rowloterias[3], rowloterias[4], rowloterias[5], rowloterias[6],
                              rowloterias[7], rowloterias[8], rowloterias[9], rowloterias[10], rowloterias[11], rowloterias[12], rowloterias[13], rowloterias[14], rowloterias[15])
            # loterias.append(loteria.__str__())
            # loteria = []

        if to_json:
            return jsonify({'loteria': loteria})
        else:
            return loteria


def VerificaJogo(tipoJogo, numConcurso, to_json=False):
    sqlCommand = """
                    select count(lot_id) from tb_lottery where lot_concurse = {0} and tpj_id = {1}
                 """.format(numConcurso, tipoJogo)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand)
    rows = result.fetchall()
    connection.close()

    if int(rows[0][0]) > 0:
        return True
    else:
        return False


def GravarJogo(loteria):
    print("Grava Jogo..")
    sqlCommand = """
                  EXEC SP_SAVE_GAME ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                 """

    formattedSQL = [int(loteria.id),
                    int(loteria.concurse),
                    str(loteria.dtConcurse.isoformat()),
                    str(loteria.game),
                    int(loteria.hit15),
                    int(loteria.hit14),
                    int(loteria.hit13),
                    int(loteria.hit12),
                    int(loteria.hit11),
                    GenericJsonEncoder.default(None, loteria.shared15),
                    GenericJsonEncoder.default(None, loteria.shared14),
                    GenericJsonEncoder.default(None, loteria.shared13),
                    GenericJsonEncoder.default(None, loteria.shared12),
                    GenericJsonEncoder.default(None, loteria.shared11),
                    str(loteria.dtNextConcurse.isoformat()),
                    int(loteria.tpj_id)
                    ]

    print("EXEC SP_SAVE_GAME {0}".format(formattedSQL))
    cursor = db.engine.raw_connection().cursor()
    cursor.execute(sqlCommand, formattedSQL)
    cursor.commit()
    print("Jogo salvo com sucesso!")
    
def ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id=0):
    params = []
    sqlCommand = """
                    SELECT 
                        count(*)
                        --pl_id, lot_id, pes_id, pl_concurse, pl_game, pl_hits, pl_ticket_amount, pl_scheduled_game, pl_game_checked 
                        FROM tb_person_lottery pl
                        inner join tb_lottery lot on lot.tpj_id = ? and lot.lot_concurse = pl.pl_concurse
                        WHERE pl.pl_concurse = ?
                        and ISNULL(pl.pl_game_checked, null) is null 
                 """
    params.append(tpj_id)
    params.append(numConcurso)
    if pes_id > 0:
        sqlCommand += " and pl.pes_id = ?"
        params.append(pes_id)

    # print(sqlCommand)
    # print(params)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand, params)
    rows = result.fetchall()
    connection.close()
    print("Retorno ContJogosPessoaSemVerificar: {0}".format(rows[0][0]))
    return int(rows[0][0])
    

# def VerificaEnvioEmailAutomatico(numConcurso, tpj_id, pes_id =0):
#     ExecuteCheckGame(numConcurso, tpj_id, pes_id)
#     print("Iniciando a verificação da SP_CHECK_GAME..")
#     connection = db.engine.connect()
#     ret = CallStoredProc(connection, 'SP_CHECK_GAME', numConcurso, tpj_id, pes_id)
#     connection.close()
#     print("Término da verificação da SP_CHECK_GAME!")
#     print("Retorno: {0}".format(ret))
#     # if int(ret) == 0:
#     #     return True
#     # else:
#     #     return False

def ExecuteCheckGame(numConcurso, tpj_id, pes_id):
    try:
        import time
        print("Iniciando a execução da SP_CHECK_GAME")
        sqlCommand = """
                    EXEC SP_CHECK_GAME ?, ?, ?
                    """
        formattedSQL = [numConcurso, tpj_id, pes_id]
        
        cursor = db.engine.raw_connection().cursor()
        cursor.execute(sqlCommand, formattedSQL)
        cursor.commit()

        # print(ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id))
        if ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id) > 0:
            while ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id=pes_id) != 0:
                # print(ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id))
                ExecuteCheckGame(numConcurso, tpj_id, pes_id)
                time.sleep(.300)

        print("Execução concluída com sucesso!")
        return True
    except Exception as ex:
        print("Ocorreu um erro ao executar oExecuteCheckGame! Erro: {0}".format(ex.args))
        return False
    
def CallStoredProc(conn, procName, *args):
    sql = """SET NOCOUNT ON;
         DECLARE @ret int
         EXEC @ret = %s %s
         SELECT @ret""" % (procName, ','.join(['?'] * len(args)))
    return int(conn.execute(sql, args).fetchone()[0])