from app.models.DAO import personDAO as _db
from app.models.tables import Person
from app.controllers.utilities import email as _emailCTRL
from app.controllers import configurationCTRL as _configCTRL
from datetime import datetime

def RecuperaPessoas(to_json=False):
    return _db.RecuperaPessoas(to_json)

def RecuperaPessoa(pes_id, to_json=False):
    return _db.RecuperaPessoa(pes_id,to_json)

def RecuperaPessoaQuePossuemJogo(num_concurse, to_json=False):
    return _db.RecuperaPessoaQuePossuemJogo(num_concurse,to_json)

def GravarPessoa(pessoaJson):
    _active = 1
    if not bool(pessoaJson['active']):
        print('Active = 0')
        _active = 0

    person = Person(None, None, None, None, None, None)
    if not pessoaJson['dtCadastro']:
        pessoaJsonData = datetime.strptime(pessoaJson['dtCadastro'], '%d/%m/%Y')
        person = Person(int(pessoaJson['id']),pessoaJson['name'], pessoaJson['email'], "",pessoaJsonData, _active)
    else:
        person = Person(int(pessoaJson['id']),pessoaJson['name'], pessoaJson['email'], "", "", _active)

    return _db.GravarPessoa(person)

def EnviaEmail(concurso, manually, pes_id):
    _objConfig = _configCTRL.RecuperaConfiguracao(pes_id, False) #VERIFICAR NO QUE QUE VAI USAR ISSO
    if _objConfig.send_email_manually:
        return _emailCTRL.EnviaEmail(concurso, _objConfig.send_email_manually, pes_id)
    else:
        return False
