from xml import dom


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        LRd=set()
        laststate=''
        pair=[float("-inf"),float("inf")]
        # 求被R和L夹住的区域
        for i in range(len(dominoes)):
            nst=dominoes[i]
            if(nst=='.'):
                continue
            if(nst=='L' and laststate=='R'):
                pair[1]=i
                LRd.add(tuple(pair))
                pair=[float("-inf"),float("inf")]
                laststate='L'
            elif(nst=='R'):
                pair[0]=i
                laststate='R'
        print(LRd)
        newdominoes=[i for i in dominoes]
        # 演算R和L夹住的区域
        for ep in LRd:
            froml=ep[0]
            fromr=ep[1]
            for i in range(froml,int((fromr+froml+1)/2)):
                newdominoes[i]="R"
            #中间不倒
            if((froml+fromr)%2==0):
                newdominoes[int((froml+fromr)/2)]='T'
            for i in range(int((fromr+froml+2)/2),fromr+1):
                newdominoes[i]="L"
        # 演算其他R和L (直推直到 非. 或 到头)
        def ph(c):
            if(newdominoes[c]=='L'):
                c-=1
                while(c>=0 and newdominoes[c]=='.'):
                    newdominoes[c]='L'
                    c-=1
            elif(newdominoes[c]=='R'):
                c+=1
                while(c<=len(newdominoes)-1 and newdominoes[c]=='.'):
                    newdominoes[c]='R'
                    c+=1
        for i in range(len(newdominoes)):
            if(newdominoes[i]!='.'):
                ph(i)
        findominoes="".join(newdominoes)
        old=""
        while(findominoes!=old):
            old=findominoes
            findominoes=findominoes.replace("T",".")
        return findominoes


        # old=""
        # while(dominoes!=old):
        #     old=dominoes
        #     dominoes=dominoes.replace("R.L","T")
        #     dominoes=dominoes.replace(".L","LL")
        #     dominoes=dominoes.replace("R.","RR")
        #     dominoes=dominoes.replace("T","R.L")
        # return dominoes

            
            
        
                
                
domi="RR.L"
a=Solution()
print(a.pushDominoes(domi))
