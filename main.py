import math

def soma_matriz(m1, m2):
	col = len(m1[0])
	lin = len(m1)
	if len(m1) != len(m2):
		return 0
	else:
		Madic = [[0 for c in range(col)]for l in range(lin)]
		for i in range(lin):
			for j in range(col):
				Madic[i][j] = m1[i][j] + m2[i][j]
		return Madic #matriz adicao

#Produto entre matrizes, recebe 2 matrizes (nao interessa o tamanho destas mas invalido se nao fr possivel)
def prod_matriz(m1, m2):
	col = len(m1[0]) #numero de colunas
	lin = len(m2) #numero de linhas
	Mprod = [[0 for c in range(col)]for l in range(lin)] #inicializaacao dos espacos da matriz produto com numeroi de colunas do m1 e linhas do m2
	a = 0 #guarda a soma

	for i in range(lin):
		for j in range(col):
			a = 0
			for k in range (len(m1[0])):
				a += m1[i][k]*m2[k][j]
			Mprod[i][j] = a
	return Mprod #matriz produto

def ler_matriz():
	M =[] #matriz final, inicializacao
	dim = int(input("Insira a dimensao da matriz: ")) #dimensao da matriz
	print("Insira a matriz por cada linha: ")
	for i in range(dim):
		v = [int(x) for x in input("Insira a Linha nr "+ str(i+1) +": ").split()]
		M.append(v)
	return M

listaPontos = [] #lista para guarar os pontos todos
numeroPontos = int(input("Quantos pontos quer inserir? ")) # pedir o numero de pontos que o utilizador quer
for i in range(numeroPontos): #loop para dar input dos pontos
	ponto = [int(x) for x in input("Insira as 3 coordenadas separadas por espaços: ").split()]
	#as tres coordenadas
	ponto.append(1)
	#no fim de cada ponto inserir o 1 para fazer multiplicacao com as matrizes 4x4
	listaPontos.append(ponto)
	#inserir o ponto na lista de pontos na ultima posição

print(listaPontos)

#lista para selecionar a transformacao
#serie de prints para cada transformacao etc...
print("Translação simples ------- 1")
print("Rotação em torno de eixo - 2")
print("Escala ------------------- 3")
print("Reflexao num dos planos -- 4")
print("Tesoura ------------------ 5")
print("Mais que 1 operacao ------ 6")
opcao = input("O que quer fazer?: ")# pedir opcao
while opcao >= 6 == True and opcao <= 0 == True:
	if opcao == 6:
        multOperacoes = [int(x) for x in input("Insira o numero das operacoes separadas por espacos").split()]
	elif opcao == 5:
	    print("5")
	elif opcao == 4:
        print("4")
	elif opcao == 3:
        print("3")
	elif opcao == 2:
        print("2")
	elif opcao == 1:
		vetorTranslacao = [int(x) for x in input("Insira o vetor de translacao (3 coordenadas separadas)")]

	elif opcao == "big chungus":
		print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
	else:
		print("Numero invalido.\n")
		opcao = input("O que quer fazer?: ")# pedir opcao
