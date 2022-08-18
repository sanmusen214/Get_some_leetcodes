class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=version1.split(".")
        len_1=len(ver1)
        ver2=version2.split(".")
        len_2=len(ver2)
        ptr=0
        while(ptr<len_1 or ptr<len_2):
            if(ptr>=len_1 and ptr<len_2):
                while(ptr<len_2):
                    if int(ver2[ptr])>0:
                        return -1
                    ptr+=1
                return 0
            if(ptr>=len_2 and ptr<len_1):
                while(ptr<len_1):
                    if int(ver1[ptr])>0:
                        return 1
                    ptr+=1
                return 0
            if(int(ver1[ptr])>int(ver2[ptr])):
                return 1
            elif(int(ver1[ptr])<int(ver2[ptr])):
                return -1
            ptr+=1
        return 0
    
a=Solution()
print(a.compareVersion("1.0","1.0.0"))
                