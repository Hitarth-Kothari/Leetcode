# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = {0}
        dq = deque()
        dq.append(root)
        root.val = 0
        while dq:
            node = dq.popleft()
            if node.left:
                node.left.val = 2*node.val + 1
                dq.append(node.left)
                self.values.add(node.left.val)
            if node.right:
                node.right.val = 2*node.val + 2
                dq.append(node.right)
                self.values.add(node.right.val)

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
