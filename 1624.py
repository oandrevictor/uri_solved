# -*- coding: utf-8 -*-
n= 1
while n>0:
	n = int(raw_input())
	if n==0:
		break
	pesos = []
	precos = []
	for i in range(n):  
		preco, peso = map(int,raw_input().split())
		pesos.append(peso)
		precos.append(preco)
	m= int(raw_input())
	dp = [[0 for x in range(m+1)] for y in range(n+1)] 
	dp[0][0] = 0		
	
	for i in range(n+1):
		for p in range(m+1):
			if i==0 or p ==0:
				dp[i][p] = 0
			else:
				if pesos[i-1] > p:
					dp[i][p] = dp[i-1][p]
				else:
					dp[i][p] = max(dp[i-1][p], dp[i-1][p-pesos[i-1]] + precos[i-1])
				

	print dp[n][m]
