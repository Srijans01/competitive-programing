import math
n=int(input())
stack=[n]
oprs=['*','/','+','-']
curr=0
ops=[]

n-=1
opr=oprs[curr%4]
print(opr)
while(n):
	if(curr%4<2):
		if(opr=='*'):
			stack+=(stack.pop()*n),
		else:
			stack+=(stack.pop()/n),
	else:
		stack+=n,
		ops+=oprs[curr%4]	
	curr+=1
	n-=1
	opr=oprs[curr%4]
	print(opr)
	print(stack)
stack=stack[::-1]
ops=ops[::-1]
while(ops):
	op=ops.pop()
	if(op=='+'):
		stack+=(stack.pop()+stack.pop()),
	else:
		stack+=(stack.pop()-stack.pop()),

print(math.ceil(stack[-1]))	
