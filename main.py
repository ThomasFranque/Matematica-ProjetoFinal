from math import *

def matriz_Translacao(vetor_translacao): #cria a matriz translacao para ser usada na funcao de produto de funcoes
        matriz = []
        matriz[0] = [1,0,0,vetor_translacao[0]]
        matriz[1] = [0,1,0,vetor_translacao[0]]
        matriz[2] = [0,0,1,vetor_translacao[0]]
        matriz[3] = [0,0,0,1]
        return matriz


def matriz_reflexao(plano): #cria a matriz adequada a reflexao para ser usada na funcao de produto de funcoes
        matriz = []
        print("""
Planos:
XZ.........[1]
XY.........[2]
YZ.........[3]""")
        while True:
                plano = int(input("""\nSobre qual plano pretende refletir?\n"""))
                if plano == "1":#plano XZ
                        matriz = [[1,0,0,0][0,-1,0,0][0,0,1,0][0,0,0,1]]
                elif plano == "2":#plano XY
                        matriz = [[1,0,0,0][0,1,0,0][0,0,-1,0][0,0,0,1]]
                elif plano == "3":#plano YZ
                        matriz = [[-1,0,0,0][0,1,0,0][0,0,1,0][0,0,0,1]]
                else:
                        print("Por favor escolha um plano válido.\n")
        return matriz


def matriz_rotacao(angulo, eixo): #cria matriz adequada a rotacao com o angulo e eixo que se quer fazer a mesma
        a = math.radians(angulo) #angulo precisa de estar em radianos para ser passada para a funcao cos() e sen()
        matriz = []
        eixo = int(input("\nQuer fazer a rotação em que eixo?\n"))
        angulo = int(input("Qual o ângulo da rotação?\n")) 
        while True:
                if eixo == "X":
                        matriz = [[1,0,0,0][0,cos(a),-(sen(a)),0][0,sen(a),cos(a),0][0,0,0,1]]
                elif eixo == "Y":
                        matriz = [[cos(a),0,sen(a),0][0,1,0,0][-(sen(a)),0,cos(a),0][0,0,0,1]]
                elif eixo == "Z":
                        matriz = [[cos(a),-(sen(a)),0,0][sen(a),cos(a),0,0][0,0,1,0][0,0,0,1]]
                else:
                        print("Por favor escolha um eixo válido.\n")
        return matriz


def matriz_tesoura(desvioA,desvioB, eixo): #cria matriz adequada a tesoura com os 2 desvios do utilizador e o eixo em que se pretende fazer
        matriz = []
        if eixo == "X":
                 matriz = [[1,desvioA,desvioB,0][0,1,0,0][0,0,1,0][0,0,0,1]]       
        elif eixo == "Y":
                matriz = [[1,0,0,0][desvioA,1,desvioB,0][0,0,1,0][0,0,0,1]]  
        elif eixo == "Z":
                matriz = [[1,0,0,0][0,1,0,0][desvioA,desvioB,1,0][0,0,0,1]]
        else:
                print("Por favor escolha um eixo válido.\n")
        return matriz


def matriz_escala(fator_de_escala):#cria matriz adequada para a escala de um objeto EM RELACAO A ORIGEM 
        matriz = []
        matriz = [[fator_de_escala,0,0,0][0,fator_de_escala,0,0][0,0,fator_de_escala,0][0,0,0,1]]
        return matriz


def prod_matriz(matriz_operacao, ponto): #Produto entre matrizes, recebe 2 matrizes (nao interessa o tamanho destas mas invalido se nao for possivel)
	col = len(matriz_operacao[0]) #numero de colunas
	lin = len(ponto) #numero de linhas
	ponto_apos_operacao = [[0 for c in range(col)]for l in range(lin)] #inicializaacao dos espacos da matriz produto com numero de colunas do m1 e linhas do m2
	a = 0 #guarda a soma
	for i in range(lin):
		for j in range(col):
			a = 0
			for k in range (len(matriz_operacao[0])):
				a += matriz_operacao[i][k]*ponto[k][j]
			ponto_apos_operacao[i][j] = a
	return ponto_apos_operacao #matriz produto


#quase inutil
def translação(matriz): #guess what this is
        m = matriz
        col = len(m[0]) #numero de colunas
        lin = len(m) #numero de linhas
        transVal = input("insira os valores de translação de X, Y e Z separados por espaços: ").split()
        for a in range (lin):
                m[a][0]+=int(transVal[0]) #somar X
                m[a][1]+=int(transVal[1]) #somar Y
                m[a][2]+=int(transVal[2]) #somar Z
        print(m)
        return m


#quases inutil
def reflexão(matriz): #Big chungus was here
        m = matriz
        col = len(m[0]) #numero de colunas
        lin = len(m) #numero de linhas
        print("""
Planos:
XZ.........[1]
XY.........[2]
YZ.........[3]""")
        
        while True:
                opcao = int(input("""\nSobre qual plano pretende refletir?\n>"""))

                if opcao == 3:#YZ
                        opcao = 0     #X
                        break
                elif opcao == 2:#XY
                        opcao = 2     #Z
                        break
                elif opcao == 1:#XZ
                        opcao = 1     #Y
                        break
                else:
                        print("Plano invalido.\n")
                        
        for a in range (lin):
                m[a][opcao]*= -1 #CONTA

        print(m)
        return m
                

listaPontos = [] #lista para guardar os pontos todos

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
print("Translação simples ------- 1")
print("Rotação em torno de eixo - 2")
print("Escala ------------------- 3")
print("Reflexao num dos planos -- 4")
print("Tesoura ------------------ 5")
print("Mais que 1 operacao ------ 6")

while True:
        opcao = int(input("O que quer fazer?: "))# pedir opcao
        if opcao == 6:
                multOperacoes = [int(x) for x in input("Insira o numero das operacoes separadas por espacos: ").split()]
                break
        elif opcao == 5:
                print("5")
                break
        elif opcao == 4:
                reflexão(listaPontos)#funciona na reflexão errada
                break
        elif opcao == 3:
                print("3") #NÃO FUNCIONA
                fator_de_escala = [int(x) for x in input ("Insire o factor de escala: ")]
                matriz_E = matriz_escala(fator_de_escala)
                for ponto in listaPontos:
                        prod_matriz(matriz_E, ponto)
                break
        elif opcao == 2:
                print("2")
                break
        elif opcao == 1:
                vetor_translacao = [int(x) for x in input("Insira o vetor translacao separado por espacos: ").split()]
                matriz_T = matriz_Translacao(vetor_translacao)
                for ponto in listaPontos:
                        prod_matriz(matriz_T, ponto)
                break
        else:
                print("Numero invalido.\n")

print(listaPontos)
