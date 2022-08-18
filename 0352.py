class SummaryRanges:

    def __init__(self):
        table={}#所有数字的哈希，存放0 or 1

    def addNum(self, val: int) -> None:
        if val not in self.table:
            self.table[val]=1
            # if(val!=0 and self.table[val-1] ) or (val!=10**4 and self.table[val+1]):

    def getIntervals(self):
        result=[]
        



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()