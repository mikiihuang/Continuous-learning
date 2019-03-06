class BinaryTreeNode(object):
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root


    def preOrder(self,root):
        if root == None:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)
    def midOrder(self,root):
        if root == None:
            return

        self.midOrder(root.left)
        print(root.data)
        self.midOrder(root.right)

    def postOrder(self,root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)

    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right!= None:
                queue.append(node.right)


n1 = BinaryTreeNode(data="D")
n2 = BinaryTreeNode(data="E")
n3 = BinaryTreeNode(data="F")
n4 = BinaryTreeNode(data="B", left=n1, right=n2)
n5 = BinaryTreeNode(data="C", left=n3, right=None)
root = BinaryTreeNode(data="A", left=n4, right=n5)

bt = BinaryTree(root=root)
# print('先序遍历')
# bt.preOrder(bt.root)
# #
# # bt = BinaryTree(root=root)
# print('中序遍历')
# bt.midOrder(bt.root)
# #
# # bt = BinaryTree(root=root)
# print('后序遍历')
# bt.postOrder(bt.root)
#

print('层次遍历')
bt.breadth_travel(root)