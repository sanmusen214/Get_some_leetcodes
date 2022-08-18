class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        s=list(s)
        right=len(s)-1
        vowels=['a','i','u','e','o','A','I','U','E','O']
        while(left<right):
            while(left<=len(s)-1 and s[left] not in vowels):
                left+=1
            while(right>=0 and s[right] not in vowels):
                right-=1
            if(left<right):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            else:
                break
        return "".join(s)
a=Solution()
print(a.reverseVowels("lEetcOde"))