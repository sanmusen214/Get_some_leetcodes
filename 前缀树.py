# children的下标记录键
# 节点val记录值

# children宽度
width=256

class Node:
    def __init__(self,val=None) -> None:
        self.val=val
        self.children=[None for i in range(width)]
class TrieTree:
    def __init__(self):
        self.root=Node()
        self.size=0
    def put(self,k,v):
        # 没有的时候创建，有的时候修改
        def putnode(node,k,v,i):
            if(not node):
                node=Node()
            if(i==len(k)):
                node.val=v
                return node
            c=ord(k[i])
            node.children[c]=putnode(node.children[c],k,v,i+1)
            return node
        if(not self.contains(k)):
            self.size+=1
        self.root=putnode(self.root,k,v,0)
    def remove(self,k):
        def removenode(node:Node,k,i):
            if(not node):
                return None
            if(i==len(k)):
                node.val=None
            else:
                c=ord(k[i])
                node.children[c]=removenode(node.children[c],k,i+1)
            # 判断是否要删除这个节点
            if(node.val):
                return node
            for i in range(width):
                if(node.children[i]):
                    return node
            return None
            
        if(not self.contains(k)):
            return
        self.root=removenode(self.root,k,0)
    def get(self,k):
        x=self.getNode(self.root,k)
        if(x and x.val):
            return x.val
        return None
    def contains(self,k):
        return self.get(k)!=None
    def hasprefix(self,prefix):
        # 是否有前缀为prefix的key
        return self.getNode(self.root,prefix)!=None
    def getNode(self,node:Node,key)->Node:
        # 从node开始搜索key
        p=node
        for i in range(len(key)):
            if(not p):
                return None
            c=ord(key[i])
            p=p.children[c]
        return p
    def shortestprefixof(self,query):
        p=self.root
        for i in range(len(query)):
            if not p:
                return ""
            if p.val:
                return query[0:i]
            c=ord(query[i])
            p=p.children[c]
        if(p and p.val):
            return query
        return ""
    def findallprefix(self,prefix):
        father=self.getNode(self.root,prefix)
        if(not father):
            return []
        res=[]
        def traverse(node):
            # 遍历node下所有有值节点
            if(not node):
                return
            if(node.val):
                res.append(node)
            for each in node.children:
                traverse(each)
        traverse(father)
        return res
    def hasmatch(self,query):
        # '.'表示匹配任一字符
        def matchnode(node,k,i):
            if(not node):
                return None
            if(i==len(k)):
                if(node.val):
                    return node
                return None
            if(k[i]=='.'):
                for each in node.children:
                    res=matchnode(each,k,i+1)
                    if(res):
                        return res
            else:
                c=ord(k[i])
                return matchnode(node.children[c],k,i+1)
            return None
        if(matchnode(self.root,query,0)):
            return True
        return False
        
        
        
a=TrieTree()
a.put("ab",1)
a.put("ac",1)
print([each.val for each in a.findallprefix("a")])
print(a.hasmatch("a"))
