t = input()

for q in xrange(t):
    n = input()
    v, a = map(int, raw_input().split())
    vertices = [False] * v
    for edge in xrange(a):
        a, b = map(int, raw_input().split())
        if not vertices[a]:
            vertices[a] = True
        if not vertices[b]:
            vertices[b] = True

    result = len([x for x in vertices if x == True])
    print (result - 1) * 2

