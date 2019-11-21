def s_g(grid,k):
	col,n=len(grid[0]),sum(grid,[])
	print(n)
	k=k%len(n)
	print(n[-k:])
	print(n[:-k])
	n=n[-k:]+n[:-k]
	print(n)
	# for i in range(0,len(n),col):
	# 	print(i)
	return([n[i:i+col] for i in range(0,len(n),col)])
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(s_g(grid,k))
