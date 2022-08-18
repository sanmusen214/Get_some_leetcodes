class Solution:
    def numDecodings(self, s: str) -> int:
        #存储数字，代表当前串长度对应下标和个数
        liststack={-1:1}
        def addstk(what,where,plus,muchd):
            if(muchd not in what):
                what[muchd]=0
                what[where]=0
                return
            if(where not in what):
                what[where]=plus*what[muchd]
            else:
                what[where]+=(plus*what[muchd])
        for i in range(-1,len(s)):
            thisp=i
            #不添加
            if(thisp==len(s)-1):
                return liststack[thisp]%(10**9+7) if thisp in liststack else 0
            #单独添加一个解码，解码后一位如果是则0不可以解
            if(thisp<=len(s)-2 and (thisp==len(s)-2 or s[thisp+2]!="0")):
                if(s[thisp+1]!="0" and s[thisp+1]!="*"):
                    addstk(liststack,thisp+1,1,thisp)
                elif(s[thisp+1]=="*"):
                    addstk(liststack,thisp+1,9,thisp)
            #当前位置后两位联立添加两位解码，27，28，29和30以上不可以
            if(thisp<=len(s)-3 and (thisp==len(s)-3 or s[thisp+3]!="0")):
                first=s[thisp+1]
                last=s[thisp+2]
                if(first=="*"):
                    if(last=="*"):
                        addstk(liststack,thisp+2,15,thisp)
                    elif(int(last)<=6):
                        addstk(liststack,thisp+2,2,thisp)
                    else:
                        addstk(liststack,thisp+2,1,thisp)
                elif(first=="1"):
                    if(last=="*"):
                        addstk(liststack,thisp+2,9,thisp)
                    else:
                        addstk(liststack,thisp+2,1,thisp)
                elif(first=="2"):
                    if(last=="*"):
                        addstk(liststack,thisp+2,6,thisp)
                    elif(int(last)<=6):
                        addstk(liststack,thisp+2,1,thisp)

                


a=Solution()
print(a.numDecodings("6*6**40**"))
