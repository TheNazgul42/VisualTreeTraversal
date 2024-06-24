import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value] if root else []

def plot_tree(root):
    def add_edges(node, graph, pos={}, x=0, y=0, layer=1):
        if node:
            pos[node.value] = (x, -y)
            graph.add_node(node.value)
            if node.left:
                graph.add_edge(node.value, node.left.value)
                l = x - 1 / layer
                pos.update(add_edges(node.left, graph, pos=pos, x=l, y=y + 1, layer=layer + 1))
            if node.right:
                graph.add_edge(node.value, node.right.value)
                r = x + 1 / layer
                pos.update(add_edges(node.right, graph, pos=pos, x=r, y=y + 1, layer=layer + 1))
        return pos

    graph = nx.DiGraph()
    pos = add_edges(root, graph)
    labels = {node: node for node in graph.nodes()}

    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=2000, node_color='skyblue', font_size=16,
            font_weight='bold')
    plt.show()

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