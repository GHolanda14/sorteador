import random

print("###SORTEADOR DE GRUPOS SEM REPETIÇÃO###")

qntNomes = int(input("Quantidade de nomes a serem sorteados: "))
nomes = input("Nomes separados por virgula: ")
#nomes = "valerie,phyx,bjor,algus,kisha,trandir,cassius,wedro"
nomes = nomes.split(',')
sortear = 1

while(sortear == 1 and len(nomes) >= qntNomes):
	nomes.sort()
	grupo = random.sample(nomes,k=qntNomes)
	for nome in grupo:
		nomes.remove(nome)
	print(grupo)
	sortear = int(input("sortear novamente? 1 - sim, 2 - não"))

if(len(nomes) < qntNomes):
	print("Quantidade de nomes insuficientes")
