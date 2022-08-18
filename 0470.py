import random
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
def rand7():
    return random.randint(1,7)

class Solution:
    def rand10(self):
        # 1.2.3.4.5.6.7 *10
        # 1.2.3.4.5.6.7.8.9.10 *7
        """
        :rtype: int
        """
        a=rand7()
        b=rand7()
        c=rand7()
        d=rand7()
        if(c*d==49):return 10
        ref={(1, 1): 1, (1, 2): 1, (2, 1): 1, (1, 3): 1, (3, 1): 1, (1, 4): 2, (2, 2): 2, (4, 1): 2, (1, 5): 2, (5, 1): 2, (1, 6): 3, (2, 3): 3, (3, 2): 3, (6, 1): 3, (1, 7): 3, (7, 1): 4, (2, 4): 4, (4, 2): 4, (3, 3): 4, (2, 5): 4, (5, 2): 5, (2, 6): 5, (3, 4): 5, (4, 3): 5, (6, 2): 5, (2, 7): 6, (7, 2): 6, (3, 5): 6, (5, 3): 6, (4, 4): 6, (3, 6): 7, (6, 3): 7, (4, 5): 7, (5, 4): 7, (3, 7): 7, (7, 3): 8, (4, 6): 8, (6, 4): 8, (5, 5): 8, (4, 7): 8, (7, 4): 9, (5, 6):9, (6, 5): 9, (5, 7): 9, (7, 5): 9, (6, 6): 10, (6, 7): 10, (7, 6): 10, (7, 7): 10}
        return ref[(a,b)]
        # mlist=[]
        # for i in range(1,8):
        #     for j in range(1,8):
        #         mlist.append([i*j,i,j])
        # mlist.sort()
        # print(mlist)
        # ref={}
        # for each in mlist:
        #     print(each[1],each[2],each[0])
        #     ref[(each[1],each[2])]=each[0]
        # print(ref)
        
        
a=Solution()
print(a.rand10())