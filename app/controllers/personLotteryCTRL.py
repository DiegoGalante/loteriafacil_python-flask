from app.models.DAO import personLotteryDAO as _db
from app.models.tables import PersonGame

def RecuperaJsonPrincipal(numConcurso):
    return _db.RecuperaJsonPrincipal(numConcurso)

def RecuperaJogoPessoa(numConcurso, pes_id, to_json=False):
    pes_id = int(pes_id)
    to_json = bool(to_json)
    return _db.RecuperaJogoPessoa(numConcurso, pes_id, to_json)

def GravaJogoPessoa(personGame):
    try:
        # print("Iniciando GravaJogoPessoa..")
        jogos=[]
        jogos.append(personGame.game)
        if len(jogos) == 1:
            # print("Pessoa com um único jogo..")
            # print(personGame.__str__())
            if VerificaJogo(personGame.game) == 0:
                _db.GravarJogo(personGame)
        else:
            # print("Pessoa com {0} jogos..".format(len(jogos)))
            for i, jogoPessoa in enumerate(personGame.game):
                # print(jogoPessoa)
                pessoa = PersonGame(personGame.id, personGame.concurse, '', jogoPessoa.game, 0, 0, personGame.pes_id)
                if VerificaJogo(pessoa.game) == 0:
                    _db.GravarJogo(pessoa)

                pessoa = PersonGame(None,None,None,None,None,None,None)
        # print("Jogo(s) da pessoa salvo com sucesso!") 
        return True
    except Exception as ex:
        print("Ocorreu um erro ao executar GravaJogoPessoa. Erro{0}".format(ex.args))
        return False
    finally:
        # print("Finalizando GravaJogoPessoa..")
        pass

def VerificaJogo(jogo, tpj_id=2):
    return _db.VerificaJogo(jogo, tpj_id=tpj_id)
            
