#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from app.controllers.utilities.utilities import Utils as _utilCTRL
from app.controllers import configurationCTRL as _configCTRL, personLotteryCTRL as _pesLotCTRL, personCTRL as _pesCTRL, lotteryGameCTRL as _lotCTRL
from app.controllers import emailSentCTRL as _emaCTRL
from app.models.tables import Person, PersonGame, EmailSent
from app.controllers.local_config import EmailAuthentication

import locale
import dateutil.parser
SHOP_CURRENCY_LOCALE = 'Portuguese_Brazil.1252'
locale.setlocale(locale.LC_ALL, SHOP_CURRENCY_LOCALE)

"""
# -*- coding: utf-8 -*-
import gmail

https:#pymotw.com/3/smtplib/

send_from = 'email@gmail.com '
password  = 'password'
# send_to   = ['receiver1@example.com', 'receiver2@example.com']
send_to   = ['email@gmail.com']
send_to_cc = None
# send_to_cc = ['alexander@sunydale.k12.ca.us','willow@sunnydale.k12.ca.us']
send_to_bcc = ['biboskbr@hotmail.com']
subject   = 'Send gmails with attachment'
text      = 'Is attached'
files     = ['C:\\Users\\bibos\\Pictures\\img.jpg']

send_mail(send_from, password, subject, text, send_to, send_to_cc, send_to_bcc, files)
"""


def EnviaEmail(objConcurso, manually, pes_id=0):
    print('Inicia metodo de mandar e-mail..')
    if _utilCTRL.CheckConnection():
        concurso = objConcurso
        
        pessoa = Person(None, None, None, None, None, None)
        jogosPessoa = PersonGame(None, None, None, None, None, None)
        pessoas = []
        if pes_id > 0:
            print("Id da pessoa informado. pes_id: {0}".format(pes_id))
            print("Recupera configuração..")
            _objConfig = _configCTRL.RecuperaConfiguracao(pes_id, False) #VERIFICAR NO QUE QUE VAI USAR ISSO

            #VERIFICA SE AS CONFIGURAÇÕES DE ENVIO DE E-MAIL ESTÃO CORRETAS
            print("Verifica se as configurações estão de acordo..")
            print("E-mail manual: {0}. Configuração de envio de e-mail automático: {1}. Configuração de envio de e-mail manual: {2}".format(manually,_objConfig.send_email_automatically, _objConfig.send_email_manually ))
            if (not manually and _objConfig.send_email_automatically) or (manually and _objConfig.send_email_manually):
                pessoa = _pesCTRL.RecuperaPessoa(pes_id, False)
                if pessoa.id > 0:
                    if _lotCTRL.ContJogosPessoaSemVerificar(concurso.concurse, 2, pessoa.id) > 0:
                        _lotCTRL.CheckGameUpdate(concurso.concurse, 2, pes_id)

                    jogosPessoa = _pesLotCTRL.RecuperaJogoPessoa(concurso.concurse, pes_id, False)
                    jogosPessoaProcessado = []
                    if _objConfig.min_amount_to_send_email > 0:
                        for jogoPessoa in jogosPessoa:
                            if jogoPessoa.amount >= _objConfig.min_amount_to_send_email:
                                jogosPessoaProcessado.append(jogoPessoa)
                    else:
                        jogosPessoaProcessado = jogosPessoa

                    print("Inicio do envio de e-mail para: {0}, referente ao concurso {1}.".format(pessoa.name, concurso.concurse))
                    return send_mail(manually, concurso, pessoa, "Serviço Agendado Lotofacil - {0}".format(pessoa.name), montaHtml(concurso,jogosPessoaProcessado), pessoa.email, None, EmailAuthentication().MINE_EMAIL)
                
        else:
            pessoas = _pesCTRL.RecuperaPessoaQuePossuemJogo(concurso.concurse)
            print("Enviando e-mail para todas as pessoas..")
            for pessoa in pessoas:
                if _lotCTRL.ContJogosPessoaSemVerificar(concurso.concurse, 2, pessoa.id) > 0:
                    _lotCTRL.CheckGameUpdate(concurso.concurse, 2, pessoa.id)

                print("Recupera configuração da pessoa: {0}..".format(pessoa.name))
                _objConfig = _configCTRL.RecuperaConfiguracao(pessoa.id, False) #VERIFICAR NO QUE QUE VAI USAR ISSO
                #VERIFICA SE AS CONFIGURAÇÕES DE ENVIO DE E-MAIL ESTÃO CORRETAS
                print("E-mail manual: {0}. Configuração de envio de e-mail automático: {1}. Configuração de envio de e-mail manual: {2}".format(manually,_objConfig.send_email_automatically, _objConfig.send_email_manually ))
                if (not manually and _objConfig.send_email_automatically) or (manually and _objConfig.send_email_manually):
                    jogosPessoa = _pesLotCTRL.RecuperaJogoPessoa(concurso.concurse, pessoa.id, False)
                    jogosPessoaProcessado = []
                    try:
                        if _objConfig.min_amount_to_send_email > 0:
                            for jogoPessoa in jogosPessoa:
                                if jogoPessoa.hits >= _objConfig.min_amount_to_send_email:
                                    jogosPessoaProcessado.append(jogoPessoa)
                        else:
                            jogosPessoaProcessado = jogosPessoa
                    except:
                        jogosPessoaProcessado = []

                    try:
                        print("Inicio do envio de e-mail para: {0} - {1}, referente ao concurso {2}.".format(pessoa.name, pessoa.email, concurso.concurse))
                        send_mail(manually, concurso, pessoa, "Serviço Agendado Lotofacil - {0}".format(pessoa.name), montaHtml(concurso,jogosPessoaProcessado), pessoa.email, None, EmailAuthentication().MINE_EMAIL)
                    except Exception as e:
                        print("Ocorreu um arro ao enviar o e-mail! Erro: {0}".format(e.args))
                    finally:
                        jogosPessoaProcessado =[]
                        jogosPessoa = []

                    
            return  True
    else:
        return False
                
        # RECUPERA O JOGO DAS PESSOAS, MONTA O HTML E SÓ ENVIA
            


def montaHtml(concursoJogo, jogosPessoa):
    abreHtml = ""
    fechaHtml = ""
    abreBody = ""
    fechaBody = ""
    abreTable = ""
    fechaTable = ""
    abreTH = ""
    abreTHColspan = ""
    fechaTH = ""
    colspanNumero = ""
    abreTR = ""
    fechaTR = ""
    htmlFinal = ""
    
    abreHtml = """<!DOCTYPE html>
                        <html>
                        <head>
                        <style>
                        table {
                            border: 1px solid black;
                            border-collapse: collapse;
                            width: 100%;
                        }
                        th, td {
                            border: 1px solid grey;
                            border-collapse: collapse;
                            padding: 5px;
                            text-align: justify;    
                        }
                        /*tr:nth-child(even) {
                            background-color: #dddddd;
                        }*/
                        </style>
                        </head>"""

    fechaHtml = "</html>"

    abreBody = "<body>"
    fechaBody = "</body>"

    abreTable = "<table>"
    fechaTable = "</table>"

    abreTR = "<tr>"
    fechaTR = "</tr>"

    abreTD = "<td>"
    fechaTD = "</td>"

    abreTH = "<th>"
    colspanNumero = "5"
    abreTHColspan = "<th colspan='" + colspanNumero + "'>"
    fechaTH = "</th>"

    #INICIA O HTML
    htmlFinal += abreHtml
    htmlFinal += abreBody

    #INICIA A TABELA
    htmlFinal += abreTable

    #PRIMEIRA LINHA
    htmlFinal += abreTR

    colspanNumero = "4"
    abreTHColspan = "<th colspan='" + colspanNumero + "'>"
    htmlFinal += abreTHColspan
    htmlFinal += "Concurso: {0}".format(concursoJogo.concurse)
    htmlFinal += fechaTH

    htmlFinal += abreTH
    htmlFinal += dateutil.parser.parse(str(concursoJogo.dtConcurse)).strftime('%d/%m/%Y') #ARRUMAR A DATA
    htmlFinal += fechaTH

    htmlFinal += fechaTR

    htmlFinal += abreTR
    colspanNumero = "5"
    abreTHColspan = "<th colspan='" + colspanNumero + "' style='text-align:center;'>"
    htmlFinal += abreTHColspan
    htmlFinal += concursoJogo.game
    htmlFinal += fechaTH
    htmlFinal += fechaTR

    headerTeable = [
                "ID",
                "Acertos",
                "Jogo",
                "Autor",
                "Valor Arrecadado"
    ]

    # HEADER Tabela
    htmlFinal += abreTR
    for coluna in headerTeable:
        htmlFinal += abreTH
        htmlFinal += coluna
        htmlFinal += fechaTH

    htmlFinal += fechaTR
    # FIM HEADER Tabela


    #MIOLODATABELA
    valorBilhetes = 0
    if len(jogosPessoa) > 0:
        for acerto in jogosPessoa:
            htmlFinal += abreTR
            htmlFinal += abreTH
            htmlFinal += "{0}".format(acerto.id)
            htmlFinal += fechaTH

            htmlFinal += "<th style='text-align:center;'>"
            htmlFinal += "{0}".format(acerto.hits)
            htmlFinal += fechaTH

            htmlFinal += abreTH
            htmlFinal += DestacaNumero(concursoJogo.game, acerto.game)
            htmlFinal += fechaTH

            htmlFinal += abreTH
            htmlFinal += acerto.name
            htmlFinal += fechaTH

            htmlFinal += "<th style='text-align:center;'>"

            if acerto.hits == 11:
                htmlFinal += locale.currency(concursoJogo.shared11, grouping = True ).replace("R$","")
                valorBilhetes += concursoJogo.shared11
            elif acerto.hits == 12:
                htmlFinal += locale.currency(concursoJogo.shared12, grouping = True ).replace("R$","")
                valorBilhetes += concursoJogo.shared12
            elif acerto.hits == 13:
                htmlFinal += locale.currency(concursoJogo.shared13, grouping = True ).replace("R$","")
                valorBilhetes += concursoJogo.shared13
            elif acerto.hits == 14:
                htmlFinal += locale.currency(concursoJogo.shared14, grouping = True ).replace("R$","")
                valorBilhetes += concursoJogo.shared14
            elif acerto.hits == 15:
                htmlFinal += locale.currency(concursoJogo.shared15, grouping = True ).replace("R$","")
                valorBilhetes += concursoJogo.shared15
            else:
                htmlFinal += locale.currency(0, grouping=True).replace("R$","")

            htmlFinal += fechaTH

            htmlFinal += fechaTR
            #FIM MIOLODATABELA
    else:
        htmlFinal += abreTR
        colspanNumero = "5"
        abreTHColspan = "<th colspan='" + colspanNumero + "' style='text-align:center;'>"
        htmlFinal += abreTHColspan
        htmlFinal += "Não há jogos válidos de acordo com sua configuração. <br/> <span style='text-decoration: underline;'> Verifique a configuração: <span style='color:red;'>\"Valor mínimo do bilhete para o envio de e-mail\"</span>, para carregar os jogos no e-mail. </span>"
        htmlFinal += fechaTH
        
    #Footer Tabela
    htmlFinal += abreTR
    colspanNumero = "4"
    abreTHColspan = "<th colspan='" + colspanNumero + "' style='text-align:right;'>"
    htmlFinal += abreTHColspan
    htmlFinal += "Quantidade a receber dos bilhetes (R$)"
    htmlFinal += fechaTH

    htmlFinal += "<th style='text-align:center; font-size:18px;'>"
    # htmlFinal += qtdeTotalARecolher > 0 ? qtdeTotalARecolher.To("N") : "0,00"
    
    htmlFinal += locale.currency(valorBilhetes, grouping=True).replace("R$","")
    htmlFinal += fechaTH
    htmlFinal += fechaTR
    # FIM Footer Tabela

    htmlFinal += fechaTable
    htmlFinal += fechaBody
    htmlFinal += fechaHtml


    return htmlFinal

def DestacaNumero(concurse, personGame):
    colorRed = "red"
    abreIns = "<ins style='color:" + colorRed + "'>"
    fechaIns = "</ins>"
    achou = False
    retorno = ""
    jogoPessoaSplit = personGame.split('-')
    jogoConcursoSplit = concurse.split('-')

    for j in range(len(jogoPessoaSplit)):
        for i in range(len(jogoConcursoSplit)):
            achou = False
            if int(jogoPessoaSplit[j]) == int(jogoConcursoSplit[i]):
                achou = True
                if j < (len(jogoPessoaSplit)-1):
                    retorno += abreIns + jogoPessoaSplit[j] + fechaIns + "-"
                else:
                    retorno += abreIns + jogoPessoaSplit[j] + fechaIns
                break
        
        if not achou:
            if j < len(jogoConcursoSplit)-1:
                retorno += jogoPessoaSplit[j] + "-" 
            else:
                retorno += jogoPessoaSplit[j]

    return retorno

def send_mail(manually, objConcurso, objPessoa,subject, text, send_to=None, send_to_cc=None, send_to_bcc=None, files=None):
    send_from = EmailAuthentication().USERNAME
    password = EmailAuthentication().PWD

    if send_to is not None:
        if type(send_to) is list:
            assert isinstance(send_to, list)
        else:
            send_to = [send_to]
            assert isinstance(send_to, list)
    if send_to_cc is not None:
        if type(send_to_cc) is list:
            assert isinstance(send_to_cc, list)
        else:
            send_to_cc = [send_to_cc]
            assert isinstance(send_to_cc, list)
    if send_to_bcc is not None:
        if type(send_to_bcc) is list:
            assert isinstance(send_to_bcc, list)
        else:
            send_to_bcc = [send_to_bcc]
            assert isinstance(send_to_bcc, list)

    msg = MIMEMultipart()
    msg['From'] = send_from

    if send_to is not None:
        msg['To'] = COMMASPACE.join(send_to)

    if send_to_cc is not None:
        msg['Cc'] = COMMASPACE.join(send_to_cc)
        if send_to is None:
            send_to = []
        send_to += send_to_cc

    if send_to_bcc is not None:
        if send_to is None:
            send_to = []
        send_to += send_to_bcc

    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'html'))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(
                f)
            msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(send_from, password)
    result = False
    try:
        print("Enviando e-mail..")
        smtp.sendmail(send_from, send_to, msg.as_string())
        result = True
        print("E-mail Enviado com sucesso!")
    except Exception as e:
        print("Ocorreu um arro ao enviar o e-mail.")
        print("Erro: {0}".format(e.args))
        # raise e
    finally:
        smtp.close()
        emailSent = EmailSent(0, 0, objPessoa.id, objPessoa.email, EmailAuthentication().MINE_EMAIL, '',  0, "Serviço Agendado Lotofacil - {0}".format(objPessoa.name), text, _pesLotCTRL.RecuperaJogoPessoa(objConcurso.concurse, objPessoa.id, True)['totalBilhetes'], objConcurso.concurse, result, manually)
        print("Gravando log do envio de e-mail!")
        _emaCTRL.GravaLog(emailSent)

    return result
