import math

def matriz_Translacao(vetor_translacao): #cria a matriz translacao para ser usada na funcao de produto de funcoes
        matriz = [[1,0,0,vetor_translacao[0]], [0,1,0,vetor_translacao[1]],[0,0,1,vetor_translacao[2]], [0,0,0,1]]
        return matriz


def matriz_reflexao(): #cria a matriz adequada a reflexao para ser usada na funcao de produto de funcoes
        matriz = []
        print("""
Planos:
XZ.........[1]
XY.........[2]
YZ.........[3]""")
        while True:
                plano = int(input("""\nSobre qual plano pretende refletir?\n"""))
                if plano == 1: #plano XZ
                        matriz = [[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]]
                        break
                elif plano == 2: #plano XY
                        matriz = [[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]
                        break
                elif plano == 3: #plano YZ
                        matriz = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
                        break
                else:
                        print("Por favor escolha um plano válido.\n")
        return matriz


def matriz_rotacao(): #cria matriz adequada a rotacao com o angulo e eixo que se quer fazer a mesma
        matriz = []       
        angulo = int(input("Qual o ângulo da rotação?\n")) 
        a = math.radians(angulo) #angulo precisa de estar em radianos para ser passada para a funcao cos() e sen()

        while True:
                eixo = input("\nQuer fazer a rotação em que eixo? Insira X, Y ou Z.\n") 
                if eixo == "X":
                        matriz = [[1,0,0,0],[0,math.cos(a),-(math.sin(a)),0],[0,math.sin(a),math.cos(a),0],[0,0,0,1]]
                        break
                elif eixo == "Y":
                        matriz = [[math.cos(a),0,math.sin(a),0],[0,1,0,0],[-(math.sin(a)),0,math.cos(a),0],[0,0,0,1]]
                        break
                elif eixo == "Z":
                        matriz = [[math.cos(a),-(math.sin(a)),0,0],[math.sin(a),math.cos(a),0,0],[0,0,1,0],[0,0,0,1]]
                        break
                else:
                        print("Por favor escolha um eixo válido.\n")
        return matriz


def matriz_tesoura(desvioA, desvioB): #cria matriz adequada a tesoura com os 2 desvios do utilizador e o eixo em que se pretende fazer
        matriz = []
        
        while True:
                eixo = input("\nQuer fazer a tesoura em que eixo? Insira X, Y ou Z.\n")
                if eixo == "X":
                        matriz = [[1,desvioA,desvioB,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
                        break
                elif eixo == "Y":
                        matriz = [[1,0,0,0],[desvioA,1,desvioB,0],[0,0,1,0],[0,0,0,1]]
                        break
                elif eixo == "Z":
                        matriz = [[1,0,0,0],[0,1,0,0],[desvioA,desvioB,1,0],[0,0,0,1]]
                        break
                else:
                        print("Por favor escolha um eixo válido.\n")
        return matriz


def matriz_escala(fator_de_escala): #cria matriz adequada para a escala de um objeto EM RELACAO A ORIGEM 
        matriz = []
        matriz = [[fator_de_escala,0,0,0],[0,fator_de_escala,0,0],[0,0,fator_de_escala,0],[0,0,0,1]]
        return matriz


def prod_matriz(matriz_operacao, matriz_operacao2): #Produto entre matrizes, recebe 2 matrizes (nao interessa o tamanho destas mas invalido se nao for possivel)
    col = len(matriz_operacao[0]) #numero de colunas
    lin = len(ponto) #numero de linhas
    matriz_operacao_final = [[0 for c in range(col)]for l in range(lin)] #inicializaacao dos espacos da matriz produto com numero de colunas do m1 e linhas do m2
    a = 0 #guarda a soma
    for i in range(lin):
        for j in range(col):
            a = 0
            for k in range (len(matriz_operacao[0])):
                a += matriz_operacao[i][k]*matriz_operacao2[k][j]
            matriz_operacao_final[i][j] = a
    return matriz_operacao_final #matriz produto

def prod_matriz_ponto (matriz_operacao, ponto):
    col = len(matriz_operacao)
    lin = len(ponto)
    ponto_apos_operacao= [[0 for c in range(col)] for l in range(lin)]
    a= 0
    for i in range(lin):
                      a = 0
                      for j in range(col):
                              a += matriz_operacao[i][j]*ponto[j]
                      ponto_apos_operacao[i] = a
    return ponto_apos_operacao

listaPontos = [] #lista para guardar os pontos todos
novaListaPontos= []
listaMatrizes = []
counter = 0
numeroPontos = int(input("Quantos pontos quer inserir? ")) # pedir o numero de pontos que o utilizador quer
for i in range(numeroPontos): #loop para dar input dos pontos
    ponto = [int(x) for x in input("Insira as 3 coordenadas separadas por espaços: \n ").split()]
    #as tres coordenadas
    ponto.append(1)
    #no fim de cada ponto inserir o 1 para fazer multiplicacao com as matrizes 4x4
    listaPontos.append(ponto)
    #inserir o ponto na lista de pontos na ultima posição

print(listaPontos)
#listaPontos = MATRIZ nao, isto nao e verdade, a lista de pontos e unicamente para guardar os pontos inseridos pelo utilizador, nao pode ser usada para contas diretamente, apenas para recolher os pontos.


#lista para selecionar a transformacao
#serie de prints para cada transformacao etc...
print("""
Translação simples ---------- 1
Rotação em torno de eixo - 2
Escala ---------------------------- 3
Reflexao num dos planos -- 4
Tesoura --------------------------- 5
Mais que 1 operacao -------- 6""")

while True:
        opcao = int(input("O que quer fazer?: "))# pedir opcao
        if opcao == 6:
                multOperacoes = [int(x) for x in input("Insira as operacoes separadas por espacos: ").split()]
                for operacao in multOperacoes:
                        counter += 1
                        if operacao == 1:
                                vetor_translacao = [int(x) for x in input("Insira o vetor translacao separado por espacos: ").split()]
                                matriz = matriz_Translacao(vetor_translacao)
                                listaMatrizes.append(matriz)
                        elif operacao == 2:
                                matriz = matriz_rotacao()
                                listaMatrizes.append(matriz)
                        elif operacao == 3:
                                fator_de_escala = int(input("Insire o factor de escala: "))
                                matriz = matriz_escala(fator_de_escala)
                                listaMatrizes.append(matriz)
                        elif operacao == 4:
                                matriz = matriz_reflexao()
                                listaMatrizes.append(matriz)
                        elif operacao == 5:
                                desvioA = int(input("Insire o primeiro desvio: "))
                                desvioB = int(input("Insire o segundo desvio: "))
                                matriz = matriz_tesoura(desvioA, desvioB)
                                listaMatrizes.append(matriz)

                for i in range(counter):
                        if i == 0:
                               matriz = prod_matriz(listaMatrizes[i], listaMatrizes[i+1])
                        elif (i%2 == 0) :
                                matriz = prod_matriz(matriz, listaMatrizes[i])
                        elif (i == counter-1) and (i%2 != 0):
                                matriz = prod_matriz(matriz, listaMatrizes[i])
                for ponto in listaPontos:
                        novoPonto = prod_matriz_ponto(matriz,ponto)
                        novaListaPontos.append(novoPonto)
                break
        elif opcao == 5:
                desvioA = int(input("Insire o primeiro desvio: "))
                desvioB = int(input("Insire o segundo desvio: "))
                matriz = matriz_tesoura(desvioA, desvioB)
                for ponto in listaPontos:
                        novoPonto = prod_matriz_ponto(matriz,ponto)
                        novaListaPontos.append(novoPonto)
                break
        elif opcao == 4:
                matriz = matriz_reflexao()
                for ponto in listaPontos:
                        novoPonto = prod_matriz_ponto(matriz,ponto)
                        novaListaPontos.append(novoPonto)
                break
        elif opcao == 3:
                fator_de_escala = int(input("Insire o factor de escala: "))
                matriz = matriz_escala(fator_de_escala)
                for ponto in listaPontos:
                        novoPonto = prod_matriz_ponto(matriz, ponto)
                        novaListaPontos.append(novoPonto)
                break
        elif opcao == 2:
                matriz = matriz_rotacao()
                for ponto in listaPontos:
                        novoPonto = prod_matriz_ponto(matriz, ponto)
                        novaListaPontos.append(novoPonto)
                break
        elif opcao == 1:
                vetor_translacao = [int(x) for x in input("Insira o vetor translacao separado por espacos: ").split()]
                matriz = matriz_Translacao(vetor_translacao)
                for ponto in listaPontos:
                        novoPonto = prod_matriz_ponto(matriz, ponto)
                        novaListaPontos.append(novoPonto)
                break
        else:
                print("Numero invalido.\n")

print(novaListaPontos)
