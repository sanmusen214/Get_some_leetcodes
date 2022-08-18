import random


class RandomizedSet:

    def __init__(self):
        self.indbook=dict()
        self.nums=[]

    def insert(self, val: int) -> bool:
        if(val not in self.indbook):
            self.indbook[val]=len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if(val in self.indbook):
            targetind=self.indbook[val]
            bereplaced=self.nums[len(self.nums)-1]
            self.indbook.pop(val)
            if(len(self.nums)!=1):
                self.indbook[bereplaced]=targetind
                self.nums[targetind],self.nums[len(self.nums)-1]=self.nums[len(self.nums)-1],self.nums[targetind]
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        randind=random.randint(0,len(self.nums)-1)
        return self.nums[randind]

a=RandomizedSet()
print(a.insert(-1))
print(a.remove(-2))
print(a.insert(-2))
print(a.getRandom())
print(a.remove(-1))
print(a.insert(-2))
print(a.getRandom())