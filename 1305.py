class Solution:
    def getAllElements(self, root1, root2):
        listfinal=[]
        def inorder(root):
            if(root.left):
                inorder(root.left)
            listfinal.append(root.val)
            if(root.right):
                inorder(root.right)
        inorder(root1)
        inorder(root2)
        listfinal.sort()
        return listfinal