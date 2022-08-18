class Node:
    def __init__(self,key=None,val=None,prev=None,next=None,count=None):
        self.val=val
        self.key=key
        self.prev=prev
        self.next=next
        self.count=count #资源访问次数
        self.num=1 #如果是次数节点的头节点，记录有多少个节点是这个次数
        
class LFUCache:

    def __init__(self, capacity: int):
        # 键:node
        self.kn=dict()

        # node链表,先按count排，再按时间排,tail是会被扔掉的方向
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

        # 次数：链表中该次数的第一个Node
        self.cn=dict()
        # 剩余容量
        self.nowcap=0
        self.maxcap=capacity
        # 最高资源访问次数
        self.maxcount=0
        # 淘汰组
        self.failhead=Node()
        self.failtail=Node()
        self.failhead.next=self.failtail
        self.failtail.prev=self.failhead
    def __str__(self) -> str:
        res=[]
        node=self.head
        while(node):
            res.append(str(node.key)+":"+str(node.count))
            node=node.next
        return ",".join(res)
    
    def move(self,node:Node,back:Node):
        # 把某个节点移动到back.prev和back中间，链表操作
        if(node==back or back.prev==node):
            return
        front=back.prev
        if(node.prev and node.next):#node本身在链表中
            # 搭接node旧关系的前后
            node.prev.next=node.next
            node.next.prev=node.prev
        # 桥接新的关系前后
        front.next=node
        node.next=back
        back.prev=node
        node.prev=front
    
    def removenode(self,node):
        #node本属于count次中，将node从count列移除，不涉及链表
        #会修改node的num
        if(node.count==0):
            return
        count=node.count
        father=self.cn[count]
        if(father.num>1):#如果旧count有多于一个节点
            if(father!=node):# 如果旧count对应的father不是现在这个node，直接修改那个father的num
                father.num-=1
            else:
                # 如果父节点就是当前，则需要将count对应的父节点往后放一格
                self.cn[count]=node.next
                self.cn[count].num=father.num-1
        else:#如果旧count只有一个节点，则self.cn删除这个count
            self.cn.pop(count)
            # 删除count（唯一的node的）映射
            return True

            
    def drag(self,node):
        count=node.count+1
        # 将某个节点移动到当前count次的第一个Node前
        if(count>self.maxcount):# 如果频率大于现有的最大频率
            # 更新maxcount
            self.maxcount=count
            # 将旧的count-1移除
            self.removenode(node)
            # 在链表内移动
            self.move(node,self.head.next)
            node.num=1
            # 设置新的self.cn
            self.cn[count]=node

        elif(count in self.cn):#如果频率没超，而且现已有count
            # 将旧的count-1更新
            self.removenode(node)
            # 添加到新的count内，更新num
            node.num=self.cn[count].num+1
            # 链表内移动
            self.move(node,self.cn[count])
            # 设置新的self.cn
            self.cn[count]=node
        elif(count not in self.cn):#如果现在没有这个count
            # 将旧的count-1更新
            nextpop=self.removenode(node)
            # 添加到新的count内，更新num
            node.num=1
            # 链表内移动
            if(count==1):
                self.move(node,self.tail)
            else:# 可能removenode时把self.cn里的count-1给pop了
                if(not nextpop):
                    self.move(node,self.cn[count-1])
            # 设置新的self.cn
            self.cn[count]=node
        node.count+=1
            
    def get(self, key: int) -> int:
        if(self.maxcap==0):
            return -1
        if(key in self.kn):
            self.drag(self.kn[key])
            return self.kn[key].val
        else:
            return -1



    def put(self, key: int, value: int) -> None:
        if(self.maxcap==0):
            return 
        if(key not in self.kn):#如果key没有
            if(self.nowcap==self.maxcap):#如果超额
                lastnode=self.tail.prev
                self.kn.pop(lastnode.key)
                self.move(lastnode,self.failtail)
                self.removenode(lastnode)
                self.nowcap-=1
                
            newnode=Node(key,value,count=0)
            self.kn[key]=newnode
            self.nowcap+=1
            self.drag(newnode)
        elif(key in self.kn):#如果key存在
            self.kn[key].val=value
            self.drag(self.kn[key])
    
    
input1='["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]'
input2='[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]'
options1=[op[1:-1] for op in input1[1:-1].split(",")]
options2=[op for op in input2[2:-2].split("],[")]
obj=None
for i in range(len(options1)):
    # print(options1[i],options2[i])
    if(options1[i]=="LFUCache"):
        obj=LFUCache(int(options2[i]))
    elif(options1[i]=="put"):
        obj.put(int(options2[i].split(",")[0]),int(options2[i].split(",")[1]))
    elif(options1[i]=="get"):
        print(obj.get(int(options2[i])))
    # print(obj)