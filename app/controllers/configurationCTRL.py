from app.models.DAO import configurationDAO as _db
from app.controllers.utilities.enums import Configuracao as _enumConfig, TipoJogo

def RecuperaConfiguracao(pes_id, to_json):
    return _db.RecuperaConfiguracao(pes_id, to_json)
    
def AtualizarDezenasSemPontuacao(valorCampo, configId, pesId):
    return _db.AtualizaCampo(valorCampo, configId, pesId, _enumConfig.CalcularDezenasSemPontuacao.value)

def AtualizarEmailManual(valorCampo, configId, pesId):
    return _db.AtualizaCampo(valorCampo, configId, pesId, _enumConfig.EmailManual.value)

def AtualizarEmailAutomatico(valorCampo, configId, pesId):
    return _db.AtualizaCampo(valorCampo, configId, pesId, _enumConfig.EmailAutomatico.value)

def AtualizarJogoOnline(valorCampo, configId, pesId):
    return _db.AtualizaCampo(valorCampo, configId, pesId, _enumConfig.VerificaJogoOnline.value)

def AtualizarValorMinimo(valorCampo, configId, pesId, valorAntigo):
    try:
        valor = float(valorCampo)
    except:
        valor = float(valorAntigo)

    return _db.AtualizaCampo(valor, configId, pesId, _enumConfig.ValorMinimoParaEnviarEmail.value)

def GravaCampo(configJson):
    valorCampo = configJson['valor_campo']
    configId = configJson['config_id']
    pesId = configJson['pes_id']
    configEnum = int(configJson['enum_config'])
    # print("valorCampo: {0}".format(valorCampo))
    # print("configId: {0}".format(configId))
    # print("pesId: {0}".format(pesId))
    # print("configEnum: {0}".format(configEnum))
    

    if configEnum == _enumConfig.CalcularDezenasSemPontuacao.value:
        # print("ENUM: {0}".format(_enumConfig.CalcularDezenasSemPontuacao.value))
        return AtualizarDezenasSemPontuacao(valorCampo, configId, pesId)

    elif configEnum == _enumConfig.VerificaJogoOnline.value:
        # print("ENUM: {0}".format(_enumConfig.VerificaJogoOnline.value))
        return AtualizarJogoOnline(valorCampo, configId, pesId)

    elif configEnum == _enumConfig.EmailManual.value:
        # print("ENUM: {0}".format(_enumConfig.EmailManual.value))
        return AtualizarEmailManual(valorCampo, configId, pesId)

    elif configEnum == _enumConfig.EmailAutomatico.value:
        # print("ENUM: {0}".format(_enumConfig.EmailAutomatico.value))
        return AtualizarEmailAutomatico(valorCampo, configId, pesId)

    elif configEnum == _enumConfig.ValorMinimoParaEnviarEmail.value:
        # print("ENUM: {0}".format(_enumConfig.ValorMinimoParaEnviarEmail.value))
        valor_antigo =0
        return AtualizarValorMinimo(valorCampo, configId, pesId, valor_antigo)
    pass

# def Gravar(conf):
#     return _db.Gravar(conf)