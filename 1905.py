t = input()
# t: numero de casos de teste

def valid_pos(i, j, matriz, vis):
    if i >= 5 or j >= 5 or i < 0 or j < 0:
        return False
    return not vis[i][j] and matriz[i][j] != 1

def dfs(i, j, matriz, vis):
    if not valid_pos(i, j, matriz, vis):
        return

    vis[i][j] = 1

    dfs(i+1, j, matriz, vis)
    dfs(i-1, j, matriz, vis)
    dfs(i, j+1, matriz, vis)
    dfs(i, j-1, matriz, vis)

for i in xrange(t):
    laby = []
    vis = [[0 for n in xrange(5)] for m in xrange(5)]

    while True:
		if len(laby) == 5:
			break
		else:
			lin = map(int, raw_input().split())
			if len(lin) > 0:
				laby.append(lin)
				
    dfs(0, 0, laby, vis)

    if vis[-1][-1] == 1:
        print "COPS"
    else:
        print "ROBBERS"
