while(True):
	n, m = map(int, raw_input().split())
	if n==m==0:
		break
	number = raw_input()
	final = ""
	stack = []
	i=0
	while (i<n):
		if len(stack) == 0:
			stack.append(number[i])
		else:
			if len(stack) + (n-i) -1  < n-m:
				stack.append(number[i])
			else:
				while(len(stack)>0 and  number[i] > stack[-1] and (len(stack) + (n-i) -1  >= n-m)):
					stack.pop()
				if len(stack) < n-m:
					stack.append(number[i])
	
		#print ''.join(str(x) for x in stack),i

		i+=1
	
	print ''.join(str(x) for x in stack)
