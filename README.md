Binary Tree Visualizer

This Python application provides an intuitive visualization of binary trees along with implementations for preorder, inorder, and postorder traversals. It leverages the matplotlib library to plot the binary tree and the networkx library to manage the tree structure as a directed graph. The visual representation helps in understanding the tree's layout and the traversal order of nodes.
TreeNode Class: A basic structure for tree nodes, including attributes for value, left child, and right child.
    Tree Traversals:
        Inorder Traversal: Visits nodes in a left-root-right manner.
        Preorder Traversal: Visits nodes in a root-left-right manner.
        Postorder Traversal: Visits nodes in a left-right-root manner.
    Visualization:
        Plot Tree: Graphically displays the binary tree using a hierarchical layout, making the tree structure clear and visually appealing.

Usage:

To use this tool, create instances of TreeNode to form your desired tree structure, then call plot_tree() with the root node. The tree, along with the traversal orders, will be displayed.
Example:

Below is a sample usage of the application:
```
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(12)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.left = TreeNode(10)
root.right.left.right = TreeNode(11)
root.right.right = TreeNode(15)
root.right.right.right = TreeNode(16)
root.right.right.right.left = TreeNode(17)
root.left.right.left = TreeNode(4)
plot_tree(root)

print("Pre order: ", preorder_traversal(root))
print("In order:", inorder_traversal(root))
print("Post order:", postorder_traversal(root))
```
