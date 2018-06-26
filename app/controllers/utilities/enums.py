#!/usr/bin/env python3
# """
# How to use:
# 1º - import
# from app.controllers.utilities.enums import getEnumJogo
# 2º call method
# getEnumJogo(2)
# getEnumJogo(2).name
# getEnumJogo(2).type
# """
# from collections import namedtuple

# jogos = []
# Jogo = namedtuple('Jogo', 'name type')
# jogos.append(Jogo(name=['mega sena','megasena'], type=1))
# jogos.append(Jogo(name=['lotofacil','lotofácil', 'loto fácil', 'loto facil'], type=2))


# def getEnumJogo(tipoJogo):
#     for jogo in jogos:
#         try:
#             if tipoJogo == jogo.type or str(tipoJogo.lower()) in jogo.name:
#                 return jogo
#                 break
#         except Exception as e:
#             return None


from enum import Enum
"""
    how to use
    #  from enums import Enums

    # print(Enums(1))             //Enum.megasena
    # print(Enums['megasena'])    //Enum.megasena
    # print(Enums.megasena)       //Enum.megasena
    # print(Enums.megasena.value) //1
"""

class TipoJogo(Enum):
    """
    how to use
    #  from enums import Enums

    # print(Enums(1))             //Enum.megasena
    # print(Enums['megasena'])    //Enum.megasena
    # print(Enums.megasena)       //Enum.megasena
    # print(Enums.megasena.value) //1
    """
    megasena = 1
    lotofacil = 2
    _megasena = 'Mega Sena'
    _lotofacil = 'Loto Fácil'

class Configuracao(Enum):
    """
    how to use
    #  from enums import Enums

    # print(Enums(1))             //Enum.megasena
    # print(Enums['megasena'])    //Enum.megasena
    # print(Enums.megasena)       //Enum.megasena
    # print(Enums.megasena.value) //1
    """
    CalcularDezenasSemPontuacao = 1
    EmailManual = 2
    ValorMinimoParaEnviarEmail = 3
    EmailAutomatico = 4
    VerificaJogoOnline = 5
    



# class Enums():
#     def megasena():
#         return 1
#     megasena = staticmethod(megasena)

#     def lotofacil():
#         return 2
#     lotofacil = staticmethod(lotofacil)]