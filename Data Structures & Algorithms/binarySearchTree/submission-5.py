class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert_tree(self, node, key, val):
        if not node:
            return TreeNode(key, val)
        if node.key > key:
            node.left = self.insert_tree(node.left, key, val)
        elif node.key < key:
            node.right = self.insert_tree(node.right, key, val)
        else:
            node.val = val
        return node

    def insert(self, key: int, val: int) -> None:

        self.root = self.insert_tree(self.root, key, val)

    def find(self, node, key):
        if not node:
            return -1
        if node.key > key:
            val = self.find(node.left, key)
        elif node.key < key:
            val = self.find(node.right, key)
        else:
            return node.val
        return val

    def get(self, key: int) -> int:

        return self.find(self.root, key)

    def findMinNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMin(self) -> int:

        minNode = self.findMinNode(self.root)
        if minNode:
            return minNode.val
        else:
            return -1

    def findMax(self, root):
        curr = root
        while curr and curr.right:
            curr = curr.right
        return curr

    def getMax(self) -> int:

        maxNode = self.findMax(self.root)
        if maxNode:
            return maxNode.val
        else:
            return -1

    def remove_treenode(self, node, key):
        if not node:
            return None
        if node.key > key:
            node.left = self.remove_treenode(node.left, key)
        elif node.key < key:
            node.right = self.remove_treenode(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                minNode = self.findMinNode(node.right)
                minKey, minVal = minNode.key, minNode.val
                node.key, node.val = minKey, minVal
                node.right = self.remove_treenode(node.right, minKey)
        return node

    def remove(self, key: int) -> None:

        self.root = self.remove_treenode(self.root, key)

    def get_ordered_keys(self, node, keys):
        if not node:
            return None
        self.get_ordered_keys(node.left, keys)
        keys.append(node.key)
        self.get_ordered_keys(node.right, keys)

    def getInorderKeys(self) -> List[int]:
        keys = []
        self.get_ordered_keys(self.root, keys)
        return keys