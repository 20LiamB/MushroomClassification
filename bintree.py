import math


class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def createFromArray(self, arr):
        depth = math.log(len(arr))
        tree = TreeNode(arr[0], None, None)
        i = 0
        curr = tree
        j = 0
        while i < depth and j < len(arr):
            curr.left = arr[j]




def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root.val is None:
        return TreeNode(None, None, None)
    else:
        visited = []
        q1 = []
        q2 = []
        tree = TreeNode(root.val, None, None)

        q1.append(root)
        q2.append(tree)
        while q1:
            curr1 = q1.pop(0)
            curr2 = q2.pop(0)
            if curr1 is not None:
                curr2.left = curr1.right
                curr2.right = curr1.left
                if curr1.right not in visited:
                    q1.append(curr1.right)
                    q2.append(curr2.left)
                if curr1.left not in visited:
                    q1.append(curr1.left)
                    q2.append(curr2.right)
        return tree


if __name__ == '__main__':

    print(invertTree(tree))
