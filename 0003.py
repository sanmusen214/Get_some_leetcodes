class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
    #     width=0
    #     for left in range(len(s)):      #循环遍历左边界
    #         legal=1
    #         while(width+left+1<=len(s)):  #右边界在内的时候进入判断
    #             if(legal==0):
    #                 break
    #             for m in range(left,left+width+1):  #遍历滑块内所有元素
    #                 if(s[left:left+width+1].count(s[m])>=2):  #如果出现重复，不合法,结束遍历
    #                     legal=0
    #                     break
    #             #整个滑块内无重复就width++
    #             if(legal==1):
    #                 width+=1
    #         else:  #left+width超界，意味着最大就width
    #             return width
    #     return width
        

a=Solution()
# print(a.lengthOfLongestSubstring(""))
# print(a.lengthOfLongestSubstring(" "))
print(a.lengthOfLongestSubstring("abcb"))
print(a.lengthOfLongestSubstring("audra"))
