class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        tables={}
        tableg={}
        for p in range(len(secret)):
            if(secret[p]==guess[p]):
                bulls+=1
            else:
                if secret[p] not in tables:
                    tables[secret[p]]=1
                else:
                    tables[secret[p]]+=1
                if guess[p] not in tableg:
                    tableg[guess[p]]=1
                else:
                    tableg[guess[p]]+=1
        cows=0
        print(tables)
        print(tableg)
        for g in tableg:
            if(g in tables):
                cows+=min(tableg[g],tables[g])
        return str(bulls)+"A"+str(cows)+"B"
                    
                
            
            
            
a=Solution()
print(a.getHint("1123","0111"))
        