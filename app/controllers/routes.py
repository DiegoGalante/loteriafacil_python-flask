# -*- coding=utf-8 -*-
#!/usr/bin/env python3

from app import app, db
from flask import render_template, jsonify, json, request, url_for

from app.controllers import personCTRL as _pesCTRL, personLotteryCTRL as _pesLotCTRL, lotteryGameCTRL as _lotCTRL
from app.controllers import configurationCTRL as _configCTRL
from app.controllers.utilities.enums import TipoJogo as _enumTipoJogo

from app.models.tables import Lottery 

import requests
import time 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/players")
def players():
    return render_template('cad-pessoa.html')


@app.route("/games")
def games():
    return render_template('cad-jogo.html')


@app.route("/config")
def config():
    return render_template('config.html')


@app.route("/profile")
def profile():
    return render_template('perfil.html')


@app.route("/load", defaults={"concurse": 0}, methods=['POST'])
@app.route("/load/<concurse>", methods=['POST'])
def principal(concurse):
    try:
        t0 = time.time()
        try:
            concurse = int(concurse)
        except:
            concurse = 0
        return _pesLotCTRL.RecuperaJsonPrincipal(concurse)
    except Exception as ex:
        print("Ocorreu um erro executar o processo principal. Error: {0}".format(ex.args))
        concurse = 0
    finally:
        print("Tempo da execução do load: {0}".format(time.time()-t0))

@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    try:
        t0 = time.time()
        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            objJson = request.get_json()

            if  _pesCTRL.EnviaEmail(_lotCTRL.RecuperaJogo(_enumTipoJogo.lotofacil.value,int(objJson['concurse']['concurse']),False), True, int(objJson['configuration']['person'])):
                return jsonify({'return': True, 'msg': 'E-mail enviado com sucesso!'})
            else:
                return jsonify({'return': False, 'msg' : "Ocorreu um erro ao enviar o e-mail. Por favor, tente novamente mais tarde ou contate o desenvolvedor."})
        else:
            return jsonify({'result': False})

    except Exception as ex:
        print(ex.args)
        return jsonify({'return': False, 'msg' : "Ocorreu um erro realizar o processo. Error: {0}".format(ex.args)})
    finally:
        print("Tempo da execução do sendEmail: {0}".format(time.time()-t0))


    

@app.route("/checkOnline/<checkOnline>", methods=['POST'])
def checkJogoOnline(checkOnline):
    try:
        t0 = time.time()
        # da pra melhorar isso aqui
        # usar  objeto de configuracao e ver se a config de verificar jogo online está ativada
        if checkOnline and request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            checkJson = request.get_json()
            if _configCTRL.RecuperaConfiguracao(int(checkJson['configuration']['person']), False).check_game_online:
                checkOnline = bool(checkOnline)
                _lotCTRL.VerificaJogoOnline(checkOnline, int(checkJson['configuration']['person']))

        return jsonify({'return': True, 'msg': 'Dados Atualizados com sucesso!'})
    except Exception as ex:
        print("Ocorreu um erro executar o processo checkJogoOnline. Error: {0}".format(ex.args))
        return jsonify({'return': False, 'msg' : "Ocorreu um erro realizar o processo checkJogoOnline. Error: {0}".format(ex.args)})
    finally:
        print("Tempo da execução do checkJogoOnline: {0}".format(time.time()-t0))

    

@app.route("/loadGames", methods=['POST'])
def loadGames():
    try:
        t0 = time.time()
        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            objJson = request.get_json()

            lottery = Lottery(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
            lottery = _lotCTRL.RecuperaJogo(_enumTipoJogo.lotofacil.value, int(objJson['concurse']['concurse']), False)
            retornoPessoasJogo = _pesLotCTRL.RecuperaJogoPessoa(lottery.concurse, 0, to_json=True)
            # print("Pessoa Jogo")
            # print(float(retornoPessoasJogo['totalBilhetes']))
            return jsonify({'return': _lotCTRL.ProcessaJogos(lottery, None), 'msg': 'Requisição processada com sucesso!', 'personGame' : retornoPessoasJogo['pessoas'], 'amount_tickets' : float(retornoPessoasJogo['totalBilhetes']) })
        else:
            return jsonify({'return': False, 'msg' : "Não foi possível completar a requisição.", 'personGame' : [] })
    except Exception as ex:
        print("Ocorreu um erro realizar o processo loadGames. Error: {0}".format(ex.args))
        return jsonify({'return': False, 'msg' : "Ocorreu um erro realizar o processo. Error: {0}".format(ex.args), 'personGame' : [] })
    finally:
        print("Tempo da execução do loadGames: {0}".format(time.time()-t0))

@app.route("/players", defaults={"player": 0}, methods=['POST'])
@app.route("/players/<player>", methods=['POST'])
def loadPlayers(player):
    try:
        t0 = time.time()
        player = int(player)
        return _pesCTRL.RecuperaPessoas(True)
    except Exception as ex:
        print("Não rolou: {0}".format(ex.args))
        return jsonify({'players': None})
    finally:
        print("Tempo da execução do loadPlayers: {0}".format(time.time()-t0))


@app.route("/savePlayer", methods=['POST'])
def savePlayer():
    try:
        t0 = time.time()
        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            pessoaJson = request.get_json()
            _pesCTRL.GravarPessoa(pessoaJson)   
            return jsonify({'result': True})
        else:
            return jsonify({'result': False})
    except Exception as e:
        print("Não rolou: {0}".format(ex.args))
        return jsonify({'result': False})
    finally:
        print("Tempo da execução do savePlayer: {0}".format(time.time()-t0))


@app.route("/loadConfiguration", methods=['POST'])
def loadConfiguration():
    try:
        t0 = time.time()
        pessoa_Diego = 1
        return _configCTRL.RecuperaConfiguracao(pessoa_Diego, True)
    except Exception as ex:
        print("Erro ao loadConfiguration. Erro: {0}".format(ex.args))
        return jsonify({'players': None})
    finally:
        print("Tempo da execução do loadConfiguration: {0}".format(time.time()-t0))

@app.route("/saveConfiguration", methods=['POST'])
def saveConfiguration():
    try:
        t0 = time.time()
        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            configJson = request.get_json()
            if _configCTRL.GravaCampo(configJson):
                return jsonify({'result': True})
            else:
                return jsonify({'result': False})
        else:
            return jsonify({'result': False})
    except Exception as e:
        print("Erro ao saveConfiguration. Erro: {0}".format(e.args))
        return jsonify({'result': False})
    finally:
        print("Tempo da execução do saveConfiguration: {0}".format(time.time()-t0))