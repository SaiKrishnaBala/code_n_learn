# Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def convert_tree_ll(node):
            if not node or (not node.left and not node.right):
                return node, node
            st_node1, end_node1, st_node2, end_node2 = None, None, None, None
            if node.left:
                st_node1, end_node1 = convert_tree_ll(node.left)
            if node.right:
                st_node2, end_node2 = convert_tree_ll(node.right)
            if st_node1:
                node.right = st_node1
                node.left = None
            if st_node2:
                if end_node1:
                    end_node1.right = st_node2
                    end_node1.left = None
                else:
                    node.right = st_node2
                    node.left = None
            else:
                if end_node1:
                    end_node2 = end_node1
            return node, end_node2
        if not root:
            return 
        st_node, end_node = convert_tree_ll(root)
        return
