class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
a=Solution()
print(a.lengthOfLastWord(" hello world  "))
