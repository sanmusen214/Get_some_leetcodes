class Solution:
    def compress(self, chars: "List[str]") -> int:
        temp=chars[-1]
        count=1
        for i in range(len(chars)-2,-1,-1):
            if(chars[i]==temp):
                count+=1
                chars.pop(i+1)
                if(i==0):
                    for c in range(len(str(count))):
                        chars.insert(0+1+c,str(count)[c])
            else:
                if(count!=1):
                    for c in range(len(str(count))):
                        chars.insert(i+2+c,str(count)[c])
                count=1
                temp=chars[i]
                
        return len(chars)
            
            
                
                
            
a=Solution()
print(a.compress(["a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","d","d"]))