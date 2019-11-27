def splitinto(root,k):
	l,node,res=0,root,[None for i in range(k)]
	while(node):
		node=node.next
		l+=1
	length=l//k
	mod=l%k
	pre=None
	curr=root
	for i in range(k):
		res[i]=curr
		for j in range(length+(1 if mod>0 else 0)):
			pre=curr
			curr=curr.next
		if pre:
			pre.next=None
		mod-=1
	return res
