from app import db
from app.models.tables import Configuration, Person
from app.controllers.utilities.enums import Configuracao as _enumConfig
from decimal import Decimal
from flask import jsonify


def RecuperaConfiguracao(pes_id=0, to_json=False):
    if pes_id >0:
        sqlCommand = """
                select conf_id, conf_calculate_tens_without_success, conf_send_email_manually, conf_send_email_automatically, conf_check_game_online, conf_min_amount_to_send_email, pes_id from tb_configuration
                where pes_id = ?
              """
        params = [pes_id]
    else:
        sqlCommand = """
                select conf_id, conf_calculate_tens_without_success, conf_send_email_manually, conf_send_email_automatically, conf_check_game_online, conf_min_amount_to_send_email, pes_id from tb_configuration
              """       
    

    connection = db.engine.connect()
    result = connection.execute(sqlCommand, params)
    rows = result.fetchall()
    connection.close()

    configuration = Configuration(None, None, None, None, None, None, None)
    configurations = []
    # ISSO VAI DA ERRO
    if len(rows) == 1:
        _id = int(rows[0][0])
        _calculate_tens_without_success = bool(rows[0][1])
        _send_email_manually = bool(rows[0][2])
        _send_email_automatically = bool(rows[0][3])
        _check_game_online = bool(rows[0][4])
        _min_amount_to_send_email = Decimal(rows[0][5])
        _person = int(rows[0][6])

        configuration = Configuration(_id, _calculate_tens_without_success, _send_email_manually,
                                      _send_email_automatically, _check_game_online, _min_amount_to_send_email, _person)
    else:
        for row in rows:
            _id = int(row[0])
            _calculate_tens_without_success = bool(row[1])
            _send_email_manually = bool(row[2])
            _send_email_automatically = bool(row[3])
            _check_game_online = bool(row[4])
            _min_amount_to_send_email = Decimal(row[5])
            _person = int(row[6])

            configuration = Configuration(_id, _calculate_tens_without_success, _send_email_manually,
                                      _send_email_automatically, _check_game_online, _min_amount_to_send_email, _person)
            if to_json:
                configurations.append(configuration.__str__())
            else:
                configurations.append(configuration)

    if pes_id == 0:
        if to_json:
            return jsonify( { 'configuracao' : configurations })
        else:
            return configurations
    else:
        if to_json:
            return jsonify( { 'configuracao' : configuration.__str__() })
        else:
            return configuration

        
                                      



def AtualizaCampo(valorCampo, configId, pesId, enumConfig):
    sqlCommand = ""
    params = []
    if pesId > 0 and configId > 0:
        sqlCommand = "UPDATE tb_configuration SET "

        if enumConfig == _enumConfig.CalcularDezenasSemPontuacao.value:
            sqlCommand += "conf_calculate_tens_without_success = ? "
        if enumConfig == _enumConfig.EmailManual.value:
            sqlCommand += "conf_send_email_manually = ? "
        if enumConfig == _enumConfig.EmailAutomatico.value:
            sqlCommand += "conf_send_email_automatically = ? "
        if enumConfig == _enumConfig.VerificaJogoOnline.value:
            sqlCommand += "conf_check_game_online = ? "
        if enumConfig == _enumConfig.ValorMinimoParaEnviarEmail.value:
            sqlCommand += "conf_min_amount_to_send_email = ? "

        sqlCommand += " WHERE conf_id = ? and pes_id = ?"
        params = [valorCampo, configId, pesId]

        print(sqlCommand)
        print(params)

        cursor = db.engine.raw_connection().cursor()
        cursor.execute(sqlCommand, params)
        cursor.commit()

    return True
