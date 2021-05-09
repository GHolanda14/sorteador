import random
print("###SORTEIE SEU PERSONAGEM DA MASMORRA###")

listaPersonagens = "Valerie,Algus,Rugido Cinzento,Jay,Mika"
listaPersonagens = listaPersonagens.split(',')
qntJogadores = 6

while(qntJogadores > 5):
	qntJogadores = int(input("Quantidade de jogadores na mesa(máx 5): "))

	if(qntJogadores > 5):
		print("O máximo de jogadores deste RPG é 5!")
	else:
		for x in range(0,qntJogadores):
			jogador = input("\nJogador: ")
			personagem = random.choice(listaPersonagens)
			listaPersonagens.remove(personagem)
			print("Heroi: ",personagem)
