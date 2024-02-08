- A *binary tree* is a rooted in which:
	- every node has *at most* 2 children
	- the children of a node are identified as the left or right child
- The *depth* of a tree is the length of the longest path from the root node to a leaf node

- A *binary search tree* is a tree with an ordered sequence of elements
	- all left descendants of a node have values less than the node's value
	- all right descendants of a node have values greater than the node's value
![[Pasted image 20231125131359.png]]

# Binary Tree Nodes
![[Pasted image 20231125131418.png]]

# Computing the height of a node
- The height of a node is the length of it's longest path to a leaf

**Recursive Definition**
- height(node) = 0 if node is a leaf
- height(node) = 1 + max(height(left), height(right))
![[Pasted image 20231125131532.png]]

# Traversing the tree
## Pre-order Traversal
- Read the element first, then visit the children in a left-to-right order
- *"Preorder"* because we visit the parent's first, then the children

![[Pasted image 20231125131726.png]]
In order of Pre-order search: \*  +  4  2  -  5  3

![[Pasted image 20231125131840.png]]

## Inorder Traversal
- Visit the left child, then the parent, then the right child
![[Pasted image 20231125131947.png]]


# Adding to a BST
- Adding to a BST is of O(height of the tree)
![[Pasted image 20231125132336.png]]
- Add 9 + 43:
![[Pasted image 20231125132354.png]]

# Removing a node from a BST
- There can be a few different cases when removing a node, we could be removing a:
	1. Leaf
	2. Semi-Leaf
	3. A normal node, with two children (internal node)

## Case 1 (Leaf)
- Simply remove the node (delete it)

## Case 2 (Semi-Leaf)
1) Remember the semi-leaf's item (copy it)
2) Copy the element of the semi-leaf's child into the semi-leaf
3) Re-arrange the pointers
4) Wipe out the child

## Case 3 (Internal Node)
Example: we want to remove 24
![[Pasted image 20231125133933.png]]
**Method**:
1) Find the biggest element less than the element you want removed (in this case it's 22)
2) Swap that node's element and the element you want removed (22 and 24 swap places)
3) Remove the element that you want removed (24 is gone)
![[Pasted image 20231125134057.png]]

# Major Issue with a BST
- In an ideal world, the complexity of a BST is O(h), which *h* being the height of the tree
- An ideal BST looks like this:
![[Pasted image 20231125134250.png]]

- However they often very different from this, due to the constant adding and removing of nodes, BST's can become very unbalanced
- They can end up looking like this:
![[Pasted image 20231125134344.png]]
## The Solution
[[AVL Trees]]