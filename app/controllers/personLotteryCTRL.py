from app.models.DAO import personLotteryDAO as _db

def RecuperaJsonPrincipal(numConcurso):
    return _db.RecuperaJsonPrincipal(numConcurso)

def RecuperaJogoPessoa(numConcurso, pes_id, to_json=False):
    pes_id = int(pes_id)
    to_json = bool(to_json)
    return _db.RecuperaJogoPessoa(numConcurso, pes_id, to_json)