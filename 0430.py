
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def __init__(self):
        self.result=None
    def flatten(self, head: 'Node') -> 'Node':
        if(not head):
            return head
        self.result=Node(None,None,None,None)
        tore=self.result
        def dfs(thishead):
            if(thishead):
                self.result.next=Node(thishead.val,self.result,None,None)
                self.result=self.result.next
                print(thishead.val)
            else:
                return
            if(thishead.child):
                dfs(thishead.child)
                thishead.child=None
            if(thishead.next):
                dfs(thishead.next)
        dfs(head)
        tore.next.prev=None
        return tore.next
            

