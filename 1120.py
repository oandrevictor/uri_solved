while(True):
    n, valor = map(str, input().split())
    if n==valor=="0":
        break
    valor = valor.replace(n,"")
    if valor == "":
        valor = 0
    print(int(valor))
