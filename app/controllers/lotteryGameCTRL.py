from app.models.DAO import lotteryDAO as _lotBD
from flask import jsonify, json
from app.models.tables import Lottery
from app.controllers.utilities.enums import TipoJogo as _enumGameType
from app.controllers.utilities.utilities import Utils as _utilCTRL
from app.controllers.utilities import email as _emailCTRL
from app.controllers import configurationCTRL as _configCTRL
from bs4 import BeautifulSoup
import requests
from decimal import Decimal
from datetime import datetime, date
import time
from app.controllers.jsonencoder import GenericJsonEncoder
from app.controllers.local_config import Token

def RecuperaJogoSistema(tipoJogo, dtInicio, dtFim=None):
    return _lotBD.RecuperaJogoSistema(tipoJogo, dtInicio, dtFim)

def RecuperaUltimoJogo(to_json):
    return _lotBD.RecuperaUltimoJogo(to_json)

def RecuperaJogo(tipoJogo, concurso, to_json):
    return _lotBD.RecuperaJogo(tipoJogo, concurso, to_json)

def VerificaJogo(tipoJogo, concurso):
    return _lotBD.VerificaJogo(tipoJogo, concurso)

def GravarJogo(loteria):
    return _lotBD.GravarJogo(loteria)   

def VerificaJogoOnline(num_concurse, pes_id=0):
    try:
        t0 = time.time()
        pes_id = 1 #DIEGO
        _objConfiguration = _configCTRL.RecuperaConfiguracao(pes_id, False)
        lottery_atual = RecuperaUltimoJogo(False)

        try:
            num_concurse =  int(num_concurse)
            if _lotBD.VerificaJogo(_enumGameType.lotofacil.value, num_concurse):
                num_concurse = 0
        except:
            num_concurse =0

        # print("Número para o token: {0}".format(num_concurse))
        if lottery_atual.dtNextConcurse <= datetime.today() and _objConfiguration.check_game_online and _utilCTRL.CheckConnection():
            lottery = Lottery(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
            page = requests.get(Token().GetToken(num_concurse))
            # page = requests.get(_utilCTRL.GetToken())
            soup = BeautifulSoup(page.text, 'html.parser')
            resultadoJson = json.loads(str(soup))
            # print(resultadoJson)
            if int(resultadoJson['concurso']['numero']) > 0 and not _lotBD.VerificaJogo(_enumGameType.lotofacil.value, int(resultadoJson['concurso']['numero'])) and Decimal(resultadoJson['concurso']['premiacao']['acertos_14']['valor_pago'].replace('.','').replace(',','.')) > 0:
                lottery = Lottery(0, int(resultadoJson['concurso']['numero']),
                        date(int(resultadoJson['concurso']['data'].split('/')[2]), int(resultadoJson['concurso']['data'].split('/')[1]), int(resultadoJson['concurso']['data'].split('/')[0])),
                        _utilCTRL.OrganizaJogo(resultadoJson['concurso']['dezenas'], _enumGameType.lotofacil.value), 
                        int(resultadoJson['concurso']['premiacao']['acertos_15']['ganhadores']),
                        int(resultadoJson['concurso']['premiacao']['acertos_14']['ganhadores']),
                        int(resultadoJson['concurso']['premiacao']['acertos_13']['ganhadores']),
                        int(resultadoJson['concurso']['premiacao']['acertos_12']['ganhadores']),
                        int(resultadoJson['concurso']['premiacao']['acertos_11']['ganhadores']),
                        Decimal(resultadoJson['concurso']['premiacao']['acertos_15']['valor_pago'].replace('.','').replace(',','.')),
                        Decimal(resultadoJson['concurso']['premiacao']['acertos_14']['valor_pago'].replace('.','').replace(',','.')),
                        Decimal(resultadoJson['concurso']['premiacao']['acertos_13']['valor_pago'].replace('.','').replace(',','.')),
                        Decimal(resultadoJson['concurso']['premiacao']['acertos_12']['valor_pago'].replace('.','').replace(',','.')),
                        Decimal(resultadoJson['concurso']['premiacao']['acertos_11']['valor_pago'].replace('.','').replace(',','.')),
                        date(int(resultadoJson['proximo_concurso']['data'].split('/')[2]), int(resultadoJson['proximo_concurso']['data'].split('/')[1]), int(resultadoJson['proximo_concurso']['data'].split('/')[0])),
                        # Decimal(resultadoJson['proximo_concurso']['valor_estimado'].replace('.','').replace(',','.')),
                        int(_enumGameType.lotofacil.value)
                        )
                # print(lottery.__str__())
                if lottery.shared14 > 0:
                    if not _lotBD.VerificaJogo(lottery.tpj_id, lottery.concurse):
                        _lotBD.GravarJogo(lottery)
                        _emailCTRL.EnviaEmail(lottery, False, pes_id=0)
                        return True

                        #Verifica se possui dados pra enviar no email
                        # if _lotBD.VerificaEnvioEmailAutomatico(lottery.concurse, lottery.tpj_id, _objConfiguration):
                        #     ProcessaJogos(lottery, None)
                        
                        
                        
                        
                            #verifica se a configuracao está ativada para mandar email automatico
                            # if _objConfiguration.send_email_automatically:
                            #     #envia os emails da pessoa
        else:
            print("Não há novo jogo para salvar!")
    except Exception as ex:
        print("Ocorreu um erro ao fazer a verificação online. Erro: {0}".format(ex.args))
    finally:
        print("Tempo de execução do VerificaJogoOnline: {0}".format(time.time() - t0))
        return _lotBD.RecuperaUltimoJogo(True)
        
    
    
def VerificaEnvioEmailAutomatico(numConcurso, tpj_id, objConfiguracao):
    try:
        if objConfiguracao.send_email_automatically or objConfiguracao.send_email_manually:
            return _lotBD.ExecuteCheckGame(numConcurso, tpj_id, pes_id=0)
        else:
            return False
    except:
        return False

def CheckGameUpdate(numConcurso, tpj_id, pes_id):
    try:
        return _lotBD.ExecuteCheckGame(numConcurso, tpj_id, pes_id)
        # import threading
        # thread = threading.Thread(target=_lotBD.ExecuteCheckGame(1679,2,1))
        # thread.start()
        # thread.join(timeout=60)
        # return True
    except:
        return False

def ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id):
    return _lotBD.ContJogosPessoaSemVerificar(numConcurso, tpj_id, pes_id=pes_id)

def ProcessaJogos(lottery, pessoa):
    try:
        if pessoa is not None and pessoa.id > 0:
            _objConfig = _configCTRL.RecuperaConfiguracao(pessoa.id, False)
            if _objConfig.send_email_automatically:
                return _emailCTRL.EnviaEmail(lottery, True, pes_id=pessoa.id)
            else:
                return CheckGameUpdate(lottery.concurse, lottery.tpj_id, pessoa.id)
        else:
            return CheckGameUpdate(lottery.concurse, lottery.tpj_id, 0)
            # return _emailCTRL.EnviaEmail(lottery, True)
    except Exception as ex:
        print("Ocorreu um erro ao execurar ProcessaJogos. Erro: {0}".format(ex.args))
        return False
    
