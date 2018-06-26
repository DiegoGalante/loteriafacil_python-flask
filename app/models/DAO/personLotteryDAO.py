from app import db
from app.models.tables import PersonGame, JsonDashBoard
from app.models.DAO import configurationDAO as _configDB
from flask import jsonify
from decimal import Decimal


def RecuperaJsonPrincipal(numConcurso=0):
    ultimoConcurso = 0
    sqlCommand = """
                    select top 1 lot_concurse from tb_lottery order by 1 desc
                """
    connection = db.engine.connect()
    result = connection.execute(sqlCommand)
    rows = result.fetchall()
    connection.close()
    ultimoConcurso = rows[0][0]

    if numConcurso == 0 or numConcurso > ultimoConcurso:
        numConcurso = ultimoConcurso

    # numConcurso = 1650
    retornoPessoaJogo = RecuperaJogoPessoa(numConcurso,0,True)
    totalBilhetes = Decimal(0)

    jsonDashboard = JsonDashBoard(None, None, None, None, None, None, None, None,
                                  None, None, None, None, None, None, None, None, None, None, None, None)
    jsonDash = []
    lista_final = []
    sqlCommand = """
                    select * from jsonDashboard({0})
                """.format(numConcurso)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand)
    rows = result.fetchall()
    connection.close()
    for row in rows:
        _concurse = row[0]
        _dtConcurse = row[1]
        _dtExtense = row[2]
        _game = row[3]
        _hit15 = row[4]
        _shared15 = row[5]
        _percent15 = row[6]
        _hit14 = row[7]
        _shared14 = row[8]
        _percent14 = row[9]
        _hit13 = row[10]
        _shared13 = row[11]
        _percent13 = row[12]
        _hit12 = row[13]
        _shared12 = row[14]
        _percent12 = row[15]
        _hit11 = row[16]
        _shared11 = row[17]
        _percent11 = row[18]

        jsonDashboard = JsonDashBoard(_concurse, _dtConcurse, _dtExtense, _game, _hit15, _shared15, _percent15, _hit14, _shared14, _percent14,
                                      _hit13, _shared13, _percent13, _hit12, _shared12, _percent12, _hit11, _shared11, _percent11, totalBilhetes)
        # jsonDashboard = JsonDashBoard(_concurse, _dtConcurse, _dtExtense, _game, _hit15, _shared15, _percent15, _hit14, _shared14, _percent14,
        #                               _hit13, _shared13, _percent13, _hit12, _shared12, _percent12, _hit11, _shared11, _percent11, 0)
        jsonDash = jsonDashboard.__str__()
        jsonDashboard = []
    # _dict = {}
    # _dict = {'Pessoas' : pessoas}
    # jsonDash.append(_dict)
    # lista_final.append(jsonDash)
    # lista_final.append(_dict)
    # print(jsonDash)
    # print(pessoas)
    _pessoaDiego = 1
    return jsonify({'concurse': jsonDash, 'personGame': [], 'configuration': _configDB.RecuperaConfiguracao(_pessoaDiego, False).__str__()})
    # return jsonify({'concurse': jsonDash, 'configuration': _configDB.RecuperaConfiguracao(_pessoaDiego, False).__str__()})


def RecuperaJogoPessoa(numConcurso=0, pes_id=0, to_json=False):
    
    pessoa = PersonGame(None, None, None, None, None, None)
    pessoas = []
    totalBilhetes = Decimal(0)
    sqlCommand = ""
    sqlCommand = "select * from jogoPessoa(?) "
    params = []
    params = [numConcurso]
    
    if pes_id > 0:
        _pessoaDiego = 1
        _objConfiguration = _configDB.RecuperaConfiguracao(_pessoaDiego, False)
        sqlCommand += " where pes_id = ? "
        params.append(pes_id)
        print("Configuração de Calcular dezenas que não marcaram pontos: {0}".format(_objConfiguration.calculate_tens_without_success))
        if not _objConfiguration.calculate_tens_without_success:
            sqlCommand += " and pl_hits > 10 "

    sqlCommand += " order by pl_hits desc"

    # print(sqlCommand)
    # print(params)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand, params)
    rows = result.fetchall()
    connection.close()

    if len(rows) > 0:
        # print([type(PersonGame(rowPessoas[0], rowPessoas[1], rowPessoas[2], rowPessoas[3], rowPessoas[4], Decimal(rowPessoas[5]))) for rowPessoas in rows])
        for rowPessoas in rows:
            _amount = Decimal(rowPessoas[5])
            totalBilhetes += _amount

            pessoa = PersonGame(rowPessoas[0], rowPessoas[1], rowPessoas[2], rowPessoas[3], rowPessoas[4], _amount)
            if to_json:
                pessoas.append(pessoa.__str__())
            else:
                pessoas.append(pessoa)
            pessoa=[]

    # print(pessoas)
    if to_json:
        return {'pessoas': pessoas, 'totalBilhetes': totalBilhetes}
    else:
        return pessoas

    
    pessoa = PersonGame(None, None, None, None, None, None)
    pessoas = []
    totalBilhetes = Decimal(0)

    sqlCommand = ""
    sqlCommand = "select * from jogoPessoa(?) "
    param = []
    params = [numConcurso]
    
    if pes_id > 0:
        _pessoaDiego = 1
        _objConfiguration = _configDB.RecuperaConfiguracao(_pessoaDiego, False)
        if not _objConfiguration.calculate_tens_without_success:
            sqlCommand += " where pl_hits > 10 "

    sqlCommand += " order by pl_hits desc"

    connection = db.engine.connect()
    result = connection.execute(sqlCommand, params)
    rows = result.fetchall()
    connection.close()

    if len(rows) > 0:
        for rowPessoas in rows:
            _amount = Decimal(rowPessoas[5])
            totalBilhetes += _amount

            pessoa = PersonGame(rowPessoas[0], rowPessoas[1], rowPessoas[2], rowPessoas[3], rowPessoas[4], _amount)
            if to_json:
                pessoas.append(pessoa.__str__())
            else:
                pessoas.append(pessoa)
            pessoa=[]

    # print(pessoas)
    if to_json:
        return {'pessoas': pessoas, 'totalBilhetes': totalBilhetes}
    else:
        return pessoas
