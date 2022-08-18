"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Employee:
    def __init__(self,id,importance,subordinates):
        self.id=id
        self.importance=importance
        self.subordinates=subordinates
class Solution:
    def getImportance(self, employees, id: int) -> int:
        def gettotal(employees,id):
            for each in employees:
                if each.id==id:
                    if each.subordinates==[]:
                        return each.importance
                    for i in each.subordinates:
                        each.importance+=gettotal(employees,i)
                    return each.importance
            return 0
        return gettotal(employees,id)
        
            
                    
            
                    
    

                

a=Solution()
em1=Employee(1,5,[2,3])
em2=Employee(2,3,[])
em3=Employee(3,3,[])
print(a.getImportance([em1,em2,em3],1))
# [[1,2,[2]], [2,3,[]]]
# 2
# [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
# 1
