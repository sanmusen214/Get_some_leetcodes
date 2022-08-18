class Solution:
    def convert(self, s: str, numRows: int) -> str:
        listnew=[]
        ptr=numRows-1
        times=0
        tru=1
        if(numRows==1):
            return s
        for i in range(0,numRows):
            while(tru==1):
                if(times==0 and ptr-numRows+1<len(s)):
                    listnew.append(s[ptr-numRows+1])
                    ptr+=(numRows*2-2)
                elif(times==0 and ptr-numRows+1>=len(s)):
                    times+=1
                    ptr=ptr=numRows-1
                    break
                else:
                    if(times==numRows-1 and ptr<len(s)):
                        listnew.append(s[ptr])
                        ptr+=(numRows*2-2)
                    elif(times==numRows-1 and ptr>=len(s)):
                        break
                    if(times!=0 and times!=numRows-1):
                        if(ptr-numRows+1+times<len(s)):
                            listnew.append(s[ptr-numRows+1+times])
                        else:
                            times+=1
                            ptr=numRows-1
                            break
                        if(ptr+numRows-1-times<len(s)):
                            listnew.append(s[ptr+numRows-1-times])
                            ptr+=(numRows*2-2)
                        else:
                            times+=1
                            ptr=numRows-1
                            break
        return ''.join(listnew)
                
                
                    
a=Solution()
print(a.convert("PAYPALISHIRING",3))#"PAHNAPLSIIGYIR"

