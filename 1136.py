# -*- coding: utf-8 -*-
# André Victor de Andrade Lopes
# URI 1136

while(True):
    n, b = map(int,input().split())
    if n==b==0:
        break
    bolas = [int(x) for x in input().split()]
    check = [False for x in range(n+1)]

    if n+1 ==b:
        print("Y")
    elif 0 in bolas:
        i = 0
        while(i<b and False in check):
            for bola in bolas:
                absolute = abs(bolas[i]-bola)
                if absolute < n+1:
                    check[absolute] = True
            i+=1
        if not (False in check):
            print("Y")
        else:
            print("N")
    else:
        print("N")

