from app import db
from app.models.tables import Person
from flask import jsonify

def RecuperaPessoas(to_json=False):
    sqlCommand = """
                SELECT pes_id, pes_name, pes_email, pes_dtRegister, pes_active from  tb_person
                order by pes_active desc
              """
    connection = db.engine.connect()
    result = connection.execute(sqlCommand)
    rows = result.fetchall()
    connection.close()
    pessoas = []
    # pessoa = Pessoa(None, None, None, None, None)

    for row in rows:
        _id = int(row[0])
        _name = row[1]
        _email = row[2]
        _password = ""
        _dtCadastro = row[3]

        if int(row[4]) == 1:
            _active = True
        else:
            _active = False

        pessoa = Person(_id, _name, _email, _password, _dtCadastro, _active)
        if to_json:
            pessoas.append(pessoa.__str__())
        else:
            pessoas.append(pessoa)

    if to_json:
        return jsonify({'players': pessoas})
    else:
        return pessoas

def RecuperaPessoa(pes_id,to_json=False):
    sqlCommand = """
                SELECT pes_id, pes_name, pes_email, pes_dtRegister, pes_active from tb_person  
                WHERE pes_id = ?
                order by pes_active desc
              """
    param = [pes_id]
    
    connection = db.engine.connect()
    result = connection.execute(sqlCommand, param)
    rows = result.fetchall()
    connection.close()

    _id = int(rows[0][0])
    _name = rows[0][1]
    _email = rows[0][2]
    _password = ""
    _dtCadastro = rows[0][3]

    if int(rows[0][4]) == 1:
        _active = True
    else:
        _active = False

    pessoa = Person(_id, _name, _email, _password, _dtCadastro, _active)
    if to_json:
        return jsonify({'players': pessoa.__str__()})
    else:
        return pessoa


def RecuperaPessoaQuePossuemJogo(num_concurso, to_json=False):
    sqlCommand = """
                SELECT pes.pes_id, pes.pes_name, pes.pes_email, pes.pes_dtRegister, pes.pes_active from tb_person pes 
                INNER JOIN tb_person_lottery pl ON pes.pes_id = pl.pes_id
                WHERE pl.pl_concurse = ?
                GROUP BY pes.pes_id, pes.pes_name, pes.pes_email, pes.pes_dtRegister, pes.pes_active
              """
    param = [num_concurso]
    
    print(param)
    connection = db.engine.connect()
    result = connection.execute(sqlCommand, param)
    rows = result.fetchall()
    connection.close()

    pessoas = []
    # pessoa = Pessoa(None, None, None, None, None)

    for row in rows:
        _id = int(row[0])
        _name = row[1]
        _email = row[2]
        _password = ""
        _dtCadastro = row[3]

        if int(row[4]) == 1:
            _active = True
        else:
            _active = False

        pessoa = Person(_id, _name, _email, _password, _dtCadastro, _active)
        if to_json:
            pessoas.append(pessoa.__str__())
        else:
            pessoas.append(pessoa)

    if to_json:
        return jsonify({'players': pessoas})
    else:
        return pessoas

    
        


def GravarPessoa(pessoa):
    sqlCommand = ""
    params = []
    if pessoa.id > 0:
        sqlCommand = "UPDATE tb_person SET pes_name = ?, pes_email = ?, pes_active = ? WHERE pes_id = ?"
        params = [pessoa.name,
                  pessoa.email,
                  pessoa.active,
                  pessoa.id]
    else:
        sqlCommand = "INSERT INTO tb_person (pes_name, pes_email, pes_pwd, pes_active) VALUES(?,?,?,?)"
        params = [pessoa.name,
                  pessoa.email,
                  pessoa.password,
                  pessoa.active]

    print(sqlCommand)
    print(params)
    cursor = db.engine.raw_connection().cursor()
    cursor.execute(sqlCommand, params)
    cursor.commit()
