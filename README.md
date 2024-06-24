# Binary Tree Visualizer

This Python application offers an intuitive visualization of binary trees, providing clear graphical representations and implementations for preorder, inorder, and postorder tree traversals. It utilizes the `matplotlib` library to visually plot the binary tree and `networkx` to manage the tree structure as a directed graph. This tool is especially useful for understanding the layout of the tree and the sequence of node visits during different tree traversals.

## Features

### TreeNode Class
Defines the basic structure for tree nodes, which includes attributes for the node value, left child, and right child.

### Tree Traversals
- **Inorder Traversal**: Visits nodes in a left-root-right manner.
- **Preorder Traversal**: Visits nodes in a root-left-right manner.
- **Postorder Traversal**: Visits nodes in a left-right-root manner.

### Visualization
- **Plot Tree**: Graphically displays the binary tree using a hierarchical layout to clearly depict the tree structure.

## Usage

To utilize this visualization tool, create instances of `TreeNode` to construct your desired tree structure, then call `plot_tree()` with the root node as the argument. The tree structure, along with the traversal orders, will be displayed.

## Example

Here is a sample script demonstrating how to use this application:

```python
# Create tree nodes
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

# Plot the tree
plot_tree(root)

# Display traversal orders
print("Pre order:", preorder_traversal(root))
print("In order:", inorder_traversal(root))
print("Post order:", postorder_traversal(root))
