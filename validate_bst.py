# Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_bst(node):
            if not node:
                return None, None, True
            min1, max1, validity1, min2, max2, validity2 = None, None, True, None, None, True
            if node.left:
                min1, max1, validity1 = validate_bst(node.left)
            if node.right:
                min2, max2, validity2 = validate_bst(node.right)
            if not validity1 or not validity2:
                return None, None, False
            if max1:
                if max1 < node.val:
                    if min2:
                        if min2 > node.val:
                            return min1, max2, True
                        else:
                            return None, None, False
                    else:
                        return min1, node.val, True
                else:
                    return None, None, False
            else:
                if min2:
                    if min2 > node.val:
                        return node.val, max2, True
                    else:
                        return None, None, False
                else:
                    return node.val, node.val, True                
                    
        if not root:
            return True
        min1, max1, validity1 = validate_bst(root)
        return validity1
