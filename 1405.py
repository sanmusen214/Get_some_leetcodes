class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dd={}
        #dd存储次数对应字符
        for p in [[a,'a'],[b,'b'],[c,'c']]:
            dd.setdefault(p[0],[])
            dd[p[0]].append(p[1])
        w=[]
        while(1):
            # print(dd)
            if(len(w)<2 or w[-1]!=w[-2]):
                biggest=max([num for num in dd])
                biggest_val=dd[biggest][0]
            elif(len(w)>=2 and w[-1]==w[-2]):
                for each in dd:
                    if(w[-1] in dd[each]):
                        if(len(dd[each])==1):#不合法所在只有一个
                            biggest=max([h*1 for h in dd if w[-1] not in dd[h]])
                            biggest_val=dd[biggest][0]
                        else:#不合法所在有两
                            biggest=each
                            biggest_val=dd[each][0] if dd[each][0]!=w[-1] else dd[each][1]
            if(biggest==0):
                break
            w.append(biggest_val)
            #去除
            if(len(dd[biggest])==1):
                dd.pop(biggest)
            else:
                dd[biggest].remove(biggest_val)
            #更新
            if(biggest-1>=0):
                dd.setdefault(biggest-1,[])
                dd[biggest-1].append(biggest_val)
        return "".join(w)
                



a=Solution().longestDiverseString(2,4,1)
print(a)