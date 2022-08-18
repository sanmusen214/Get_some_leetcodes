from unicodedata import name


class Presum:
    # 前缀和第i位数字表示原数组[0:i-1]之和
    def __init__(self,num):
        self.presums=[0]
        for each in num:
            self.presums.append(self.presums[-1]+each)
    # 求[left,right]之和
    def sumbetween(self,left,right):
        return self.presums[right+1]-self.presums[left]
    
if __name__=="__main__":
    p=Presum([4,6,3,1,4,2])
    print(p.sumbetween(0,5))