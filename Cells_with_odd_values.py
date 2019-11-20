class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        r=[0]*n
        c=[0]*m
        for i,j in indices:
            r[i]+=1
            c[j]+=1
        row=len([k for k in r if k%2!=0])
        col=len([k for k in c if k%2!=0])
        
        total=row*(m-col)+col*(n-row)
        return total
