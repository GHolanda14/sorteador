import random

print("###SORTEADOR DE GRUPOS SEM REPETIÇÃO###")

qntNomes = int(input("Quantidade de nomes a serem sorteados: "))
qntGrupos = int(input("Quantidade de grupos: "))

nomes = input("Nomes separados por virgula: ")
nomes = nomes.split(',')

separador = ", "

if ((qntNomes * qntGrupos) - len(nomes)) <= 0:
	nomes.sort()
	for x in range(1,qntGrupos+1):
		grupo = random.sample(nomes,k=qntNomes)
		for nome in grupo:
			nomes.remove(nome)
		print("Grupo "+str(x)+": "+separador.join(grupo))
else:
	print("A quantidade de nomes é insuficiente para a quantidade de vezes que você irá sortear!")
