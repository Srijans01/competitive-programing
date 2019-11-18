#-------Author:-Srijan Sachdeva--------
def pdt(n):
	l = len(n)
	f = 1
	for i in range(1,l+1):
		if n.find(str(i)) == -1:
			f = 0
			break
	return f
 
 
newc = [0]
for i in range(1,1000001):
	newc += [ newc[-1] + pdt(str(i))]
 
 
q = int(input())
for k in range(q):
	l,r = map(int,input().split())
	print(newc[r]-newc[l-1])
