#verificar conexão com internet
import socket
#data por extenso
from datetime import datetime, date
#organiza jogo
from app.controllers.utilities.enums import TipoJogo
# get token
import requests
from bs4 import BeautifulSoup


class Utils(object):
    
    def CheckConnection():
        """Verifica se o computador está online"""  
        print("Checa Conexão..")
        confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
        for host in confiaveis:
            a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.settimeout(.5)
            try:
                b=a.connect_ex((host, 80))
                if b==0: #ok, conectado
                    print("Conexão ok!")
                    return True
            except:
                pass
            a.close()
        print("Computador offline!")
        return False
    
    def DataPorExtenso():
        """
        0- Segunda-Feira
        1- Terça-Feira
        2- Quarta-Feira
        3- Quinta-Feira
        4- Sexta-Feira
        5- Sábado
        6 - Domingo
        """
        diasDaSemana = ('Segunda-Feira', 'Terça-Feira' , 'Quarta-Feira' , 'Quinta-Feira' , 'Sexta-Feira', 'Sábado', 'Domingo')
        mesesDoAno = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

        hj = datetime.now()
        semana = date.today()
        data = diasDaSemana[semana.weekday()] + ", " + str(hj.day) + " de " + mesesDoAno[hj.month-1] +" de "+ str(hj.year) + "."
        return data.strip()

    def FormataString( mascara, valor):
        """
        Fomrata a string conforme a mascara que passar por parâmetro.
        19000000 -> FormataString("#####-###", "19000000") ->  19000-000
        """
        posicao=0
        novoValor = ""
        for masc in mascara:
            if str(masc) == "#":  
                if len(str(valor)) > posicao:
                    novoValor = novoValor + valor[posicao]
                    posicao += 1
                else:
                    break
            else:
                if len(str(valor)) > posicao:
                    novoValor = novoValor + masc
                else:
                    break
        
        return novoValor.strip()

    def OrganizaJogo(jogoJson, tipoJogo, jogoOriginal = None):
        jogos = []
        jogo = []
        dic_final = []
        
        if tipoJogo == 2:
            dic_final = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
        elif tipoJogo == 1:
            dic_final = ['0','0','0','0','0','0']

        resultado = ""
        jogo1 = ""
        #Ordena o vetor
        lista = []
        flag = False
        for x in range(len(jogoJson)):
            tamanho = len(lista)
            dezena  = int(jogoJson[x])
            # print(dezena)
            if( tamanho > 0 ):
                for y in range( tamanho ):
                    if ( dezena <= lista[y] ):
                        lista.insert( y, dezena )
                        flag = True
                        break
            if((x == 0) or (flag == False)):
                lista.append( dezena )
            else:
                flag = False
        jogoJson = lista

        if jogoOriginal is not None:
            for j, itemModificar in enumerate(jogoJson):
                if itemModificar not in dic_final:
                    for i, itemOriginal in enumerate(jogoOriginal):
                        if int(jogoJson[j]) == int(jogoOriginal[i]) and itemOriginal not in dic_final:
                            dic_final[i] = int(itemOriginal)


            dic_not_in = [x for x in jogoJson if x not in jogoOriginal]
            for i, itemD in enumerate(dic_final):
                if int(itemD) == 0:
                    for j, itemN in enumerate(dic_not_in):
                        if int(itemN) not in dic_final:
                            dic_final[i] = int(dic_not_in[j])
                            break
        
            jogoJson = dic_final
            
        if int(tipoJogo) == int(TipoJogo.lotofacil.value):
            for l in range(15):
                jogo.append(str(jogoJson[l]))
                if len(jogo) ==  15:
                    jogos.append(jogo)
                    while len(jogo1) != 44:
                        for i in range(len(jogo)):
                            if jogo1 == "":
                                if len(jogo[i].strip()) == 1:
                                    jogo1 += "0" + jogo[i].strip()
                                else:
                                    jogo1 += jogo[i].strip()
                            elif len(jogo1) % 2 == 0:
                                if len(jogo[i].strip()) == 1:
                                    jogo1 += "-0" + jogo[i].strip()
                                else:
                                    jogo1 += "-" + jogo[i].strip()
                            else:
                                if len(jogo[i].strip()) == 1:
                                    jogo1 += "-0" + jogo[i].strip()
                                else:
                                    jogo1 += "-" + jogo[i].strip()
                        jogo = []
                        # Fim do for do i
        resultado = jogo1
        jogo1 = ""
        return resultado

    def GetToken():
        try:
            pass
            #SOME API URL
        except Exception as e:
            print("Ocorreu um problema com a API. Nada em relação com o sistema.")
            # raise e
           

    def zipar( args):
        import zipfile as zipf
        import os

        with zipf.ZipFile('teste.zip','w', zipf.ZIP_DEFLATED) as z:
            for arq in arqs:
                if(os.path.isfile(arq)): # se for ficheiro
                    z.write(arq)
                else: # se for diretorio
                    for root, dirs, files in os.walk(arq):
                        for f in files:
                            z.write(os.path.join(root, f))

        zipar(['registro.py','Tudo'])
        
        