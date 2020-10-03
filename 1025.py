#coding: utf-8

def buscaBinaria(inicio, fim, valorProcurado, lista):
	
	meio = (inicio + fim) / 2
		
	if lista[meio] == valorProcurado:
		indice = meio
		while 1:
			if lista[indice] != valorProcurado: break
			if indice == -1: break
			indice -= 1
		return indice + 2
	if inicio > fim: return -1
	if lista[meio] > valorProcurado: return buscaBinaria(inicio, meio - 1, valorProcurado, lista)
	else: return buscaBinaria(meio + 1, fim, valorProcurado, lista)

case = 0

while 1:
	
	qtdMarmores, casos = map(int, raw_input().split())
	
	if qtdMarmores == 0 and casos == 0: break

	marmores = []

	for i in range(qtdMarmores):
		entrada = int(raw_input())
		marmores.append(entrada)

	marmores.sort()
	
	case += 1
	
	print "CASE# %d:" % case
	
	for i in range(casos):
		caso = int(raw_input())
		if buscaBinaria(0, qtdMarmores - 1, caso, marmores) == -1: 		
			print "%i not found" % caso
		else:
			resultado = buscaBinaria(0, qtdMarmores - 1, caso, marmores)
			print "%i found at %i" % (caso, resultado) 
