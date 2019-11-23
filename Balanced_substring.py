class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=[]
        cR,cL,c=0,0,0
        # s=s.split()
        for e in s:
            l.append(e)
            for k in l:
                if(k=='R'):
                    cR+=1
                elif(k=='L'):
                    cL+=1
                if(cR==cL):
                    c+=1
                    l.clear()
            cR,cL=0,0
        return c
