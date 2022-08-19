'''
ListNode will create single Node,
+printNode(node) will print whole ListNode after this node,
+createNode() use numlist to creat a ListNode and return the first Node,
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def printNode(node):
    print('[ ',end='')
    while(True):
        if(node==None):
            print("]")
            break
        print("{} ".format(node.val),end='')
        node=node.next

def createNode(listnum):
    if(len(listnum)==0):
        return None
    nl=ListNode(listnum[0])
    nodelist=nl
    for i in range(1,len(listnum)):
        nl.next=ListNode(listnum[i])
        nl=nl.next
    return nodelist

if __name__=='__main__':
    ab=createNode([1,2,3,4,5,8,9])
    printNode(ab)
    while(True):
        if(ab==None):
            break
        print(ab.val)
        ab=ab.next

