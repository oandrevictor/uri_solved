n, k = map(int, raw_input().split())
alunos = []
for i in xrange(n):
	alunos.append(raw_input())

alunos.sort()

print alunos[k-1]
