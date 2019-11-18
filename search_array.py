def search(mat,n,x):
	i=0
	j=0
	while(i<n):
		while(j<n):
			if(mat[i][j]==x):
				print("n found at",i,",",j)
				return 1
			else:
				j+=1
		j=0
		i+=1


	print("element not found")
	return 0

mat = [ [20, 10, 30, 40], 
        [25, 15, 35, 45], 
        [27, 37, 29, 48], 
        [32, 39, 33, 50] ] 
search(mat, 4, 29) 
