import random as rd

def main():
	num_cartas = 5
	baralho = criar_baralho()
	jogador1 = criar_jogador(baralho, num_cartas)
	jogador2 = criar_jogador(baralho, num_cartas)
	
	print("Mão do jogador 1: ")
	mostrarMao(jogador1)
	print("Mão do jogador 2: ")
	mostrarMao(jogador2)

	ganhador(jogador1, jogador2)

def criar_baralho():
	baralho = []

	for i in range(1, 14):
		for j in range(1, 5):
			baralho.append({"valor": i, "naipe": j})
			pass
		pass
	rd.shuffle(baralho)
	return baralho

def criar_jogador(baralho, num_cartas):
	jogador = []

	for i in range(0, num_cartas):
		jogador.append(baralho.pop(-1))
		pass
	return jogador

def mostrarMao(jogador):
	for i in range(0, len(jogador)):
		valor = "A" if jogador[i]["valor"] == 1 else "J" if jogador[i]["valor"] == 11 else "Q" if jogador[i]["valor"] == 12 else "K" if jogador[i]["valor"] == 13 else str(jogador[i]["valor"])
		naipe = "paus" if jogador[i]["naipe"] == 1 else "ouros" if jogador[i]["naipe"] == 2 else "espadas" if jogador[i]["naipe"] == 3 else "copas"

		print(valor + " de " + naipe)
		pass

	tipoDeMao(jogador)

def tipoDeMao(jogador):
	if (StraightFlush(jogador) > 0):
		print("Tipo de mão: Straight Flush")
	elif (Quadra(jogador) > 0):
		print("Tipo de mão: Quadra")
	elif (FullHouse(jogador) > 0):
		print("Tipo de mão: Full House")
	elif (Flush(jogador) > 0):
		print("Tipo de mão: Flush")
	elif (Sequencia(jogador) > 0):
		print("Tipo de mão: Sequência")
	elif (Trinca(jogador) > 0):
		print("Tipo de mão: Trinca")
	elif (DoisPares(jogador) > 0):
		print("Tipo de mão: Dois Pares")
	elif (UmPar(jogador) > 0):
		print("Tipo de mão: Um Par")
	else:
		print("Tipo de mão: Carta Alta")

def ganhador(j1, j2):
	v1 = max([StraightFlush(j1), Quadra(j1), FullHouse(j1), Flush(j1), Sequencia(j1), Trinca(j1), DoisPares(j1), UmPar(j1), cartaAlta(j1)])
	v2 = max([StraightFlush(j2), Quadra(j2), FullHouse(j2), Flush(j2), Sequencia(j2), Trinca(j2), DoisPares(j2), UmPar(j2), cartaAlta(j2)])
	if (v1 > v2):
		print("O vencedor é o jogador 1!")
	elif (v2 > v1):
		print("O vencedor é o jogador 2!")
	else:
		print("Empate!")

def StraightFlush(jogador): # em ordem e do mesmo naipe
	mao = colocarNaOrdem(jogador)
	valor = 0

	if (mesmoNaipe(mao) == False):
		return valor

	if (mao[0]["valor"] == 1 and mao[-1]["valor"] == 13):
		for i in range(2, len(mao)):
			if (mao[i]["valor"] != mao[i - 1]["valor"] + 1):
				return valor
			pass

		valor = 14 * (15 ** 21)

	else:
		for i in range(1, len(mao)):
			if (mao[i]["valor"] != mao[i - 1]["valor"] + 1):
				return valor
			pass

		valor = mao[-1]["valor"] * (15 ** 21)

	return valor

def Quadra(jogador): # 4 cartas de mesmo valor
	mao = colocarNaOrdem(jogador)
	valor = 0

	for i in range(2, len(mao) - 1):
		if (mao[i]["valor"] != mao[i - 1]["valor"]):
			return valor
		pass

	if (mao[0]["valor"] == mao[2]["valor"]):
		if (mao[0]["valor"] == 1):
			valor = 14 * (15 ** 20)
		else:
			valor = mao[0]["valor"] * (15 ** 20)

	elif (mao[-1]["valor"] == mao[2]["valor"]):
		valor = mao[-1]["valor"] * (15 ** 20)

	return valor

def FullHouse(jogador): # Um 'par' de 3 e um par de 2
	mao = colocarNaOrdem(jogador)
	valor = 0
		
	if (mao[0]["valor"] == mao[2]["valor"] and mao[1]["valor"] == mao[2]["valor"] and mao[3]["valor"] == mao[4]["valor"]):
		if (mao[0]["valor"] == 1):
			valor = 14 * (15 ** 19)
		else:
			valor = mao[0]["valor"] * (15 ** 19)

	elif (mao[3]["valor"] == mao[2]["valor"] and mao[4]["valor"] == mao[2]["valor"] and mao[0]["valor"] == mao[1]["valor"]):
		valor = mao[-1]["valor"] * (15 ** 19)

	return valor

def Flush(jogador): # Mesmo naipe
	mao = colocarNaOrdem(jogador)
	valor = 0

	if (mesmoNaipe(jogador)):
		if (mao[0]["valor"] == 1):
			valor = 14 * (15 ** 18)

			for i in range(1, len(mao)):
				valor += mao[i]["valor"] * (15 ** (i + 14))
				pass

		else:
			for i in range(0, len(mao)):
				valor += mao[i]["valor"] * (15 ** (i + 14))
				pass

	return valor

def Sequencia(jogador):
	mao = colocarNaOrdem(jogador)
	valor = 0

	if (mao[0]["valor"] == 1 and mao[-1]["valor"] == 13):
		for i in range(2, len(mao)):
			if (mao[i]["valor"] != mao[i - 1]["valor"] + 1):
				return valor
			pass

		valor = 14 * (15 ** 13)

	else:
		for i in range(1, len(mao)):
			if (mao[i]["valor"] != mao[i - 1]["valor"] + 1):
				return valor
			pass

		valor = mao[-1]["valor"] * (15 ** 13)

	return valor

def Trinca(jogador): # 3 cartas com mesmo valor
	mao = colocarNaOrdem(jogador)
	valor = 0

	if ((mao[1]["valor"] == mao[2]["valor"] and mao[0]["valor"] == mao[2]["valor"]) or mao[3]["valor"] == mao[2]["valor"] and mao[4]["valor"] == mao[2]["valor"]):
		valor = (mao[2]["valor"] if mao[2]["valor"] != 1 else 14) * (15 ** 12)

	return valor

def DoisPares(jogador):
	mao = colocarNaOrdem(jogador)
	valor = 0

	if (mao[0]["valor"] == mao[1]["valor"] and mao[2]["valor"] == mao[3]["valor"]):
		valor = mao[4]["valor"] * (15 ** 9)

		if (mao[0]["valor"] == 1):
			valor += mao[2]["valor"] * (15 ** 10) + 14 * (15 ** 11)
		else:
			valor += mao[0]["valor"] * (15 ** 10) + mao[2]["valor"] * (15 ** 11)

	elif (mao[0]["valor"] == mao[1]["valor"] and mao[3]["valor"] == mao[4]["valor"]):
		valor = mao[2]["valor"] * (15 ** 9)

		if (mao[0]["valor"] == 1):
			valor += mao[3]["valor"] * (15 ** 10) + 14 * (15 ** 11)
		else:
			valor += mao[0]["valor"] * (15 ** 10) + mao[3]["valor"] * (15 ** 11)

	elif (mao[1]["valor"] == mao[2]["valor"] and mao[3]["valor"] == mao[4]["valor"]):
		valor = (mao[0]["valor"] if mao[0]["valor"] != 1 else 14) * (15 ** 9) + mao[1]["valor"] * (15 ** 10) + mao[3]["valor"] * (15 ** 11)

	return valor

def UmPar(jogador):
	mao = colocarNaOrdem(jogador)
	valor = 0

	for i in range(1, len(mao)):
		if (mao[i]["valor"] == mao[i - 1]["valor"]):
			k = 5

			if (mao[0]["valor"] == 1 and i - 1 != 0):
				for j in range(1, len(mao)):
					if (j != i and j != i - 1):
						valor += mao[j]["valor"] * (15 ** k)
						k += 1
					pass

				valor += 14 * (15 ** k)
				k += 1

			else:
				for j in range(0, len(mao)):
					if (j != i and j != i - 1):
						valor += mao[j]["valor"] * (15 ** k)
						k += 1
					pass

			valor += (mao[i]["valor"] if mao[i]["valor"] != 1 else 14) * (15 ** k)
		pass

	return valor

def cartaAlta(jogador):
	mao = colocarNaOrdem(jogador)
	valor = 0

	if (mao[0]["valor"] == 1):
		valor = 14 * (15 ** 4)

		for i in range(1, len(mao)):
			valor += mao[i]["valor"] * (15 ** (i - 1))
			pass

	else:
		for i in range(0, len(mao)):
			valor += mao[i]["valor"] * (15 ** i)
			pass

	return valor

def colocarNaOrdem(jogador):
	mao = jogador[:]
	mao_final = []

	while (len(mao) > 0):
		mao_final.append(mao.pop(menor(mao)))
		pass

	return mao_final

def menor(jogador):
	j = 0

	for i in range(1, len(jogador)):
		if (jogador[i]["valor"] < jogador[j]["valor"]):
			j = i
		pass

	return j

def mesmoNaipe(jogador):
	n = jogador[0]["naipe"]

	for i in range(1, len(jogador)):
		if (jogador[i]["naipe"] != n):
			return False
		pass

	return True

main()