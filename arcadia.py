import random

qntPersonagens = int(input("Quantidade de personagens a serem sorteados: "))
qntJogadores = int(input("Quantidade de jogadores na mesa: "))

listaPersonagens = "Valerie,Phyx,Bjor,Algus,Kisha,Trandir,Cassius,Sybbyl,Izzy,Jack Jack,Jaimie,Natasha,Diana,Mark,Rei David III,Britney,Anika,Black Newt,Dris,Gabriel,Rugido Cinzento,Jay,Johnny,Mika,Príncipe Aaron,Julie,Tao"
listaPersonagens = listaPersonagens.split(",")

separador = " | "

if ((len(listaPersonagens) - (qntPersonagens * qntJogadores)) >= 0):
	listaPersonagens.sort()
	for x in range(0,qntJogadores):
		nomeJogador = input("\nJogador: ")
		selecionados = random.sample(listaPersonagens,k=qntPersonagens)
		
		for personagem in selecionados:
			listaPersonagens.remove(personagem)
		
		print("Time: "+separador.join(selecionados))
else:
	print("Quantidade de personagens insuficientes para o número de jogadores na mesa!")
