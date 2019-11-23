def first_n_smallest(arr, n):
    l=sorted(arr)[:n]
    c=0
    a=[]
    for i in arr:
        if i in l and c<n:
            a.append(i)
            l.remove(i)
            c+=1
    return a
