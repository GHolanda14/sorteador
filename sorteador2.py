import random

print("###SORTEADOR DE NOMES SEM REPETIÇÃO###")

qntNomes = int(input("Quantidade de nomes a serem sorteados: "))

nomes = input("Nomes separados por virgula: ")
nomes = nomes.split(',')
separador = ", "

while(len(nomes) >= qntNomes):
	nomes.sort()
	grupo = random.sample(nomes,k=qntNomes)
	for nome in grupo:
		nomes.remove(nome)
	print(", ".join(grupo))
	if(len(nomes) < qntNomes):
		print("Quantidade de nomes insuficientes, fim do sorteio")
		break
	else:
		sortear = int(input("sortear novamente? 1 - sim, 2 - não\n"))
		if sortear == 2:break