while True:
    try:
        n, m = map(int, raw_input().split())
        result = n ^ m
        print result
    except:
        break
