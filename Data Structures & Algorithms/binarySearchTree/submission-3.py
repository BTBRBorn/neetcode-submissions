class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def insert_tree(node, key, val):
            if not node:
                return TreeNode(key, val)
            if node.key > key:
                node.left = insert_tree(node.left, key, val)
            elif node.key < key:
                node.right = insert_tree(node.right, key, val)
            else:
                node.val = val
            return node

        self.root = insert_tree(self.root, key, val)

    def get(self, key: int) -> int:
        def find(node, key):
            if not node:
                return -1
            if node.key > key:
                val = find(node.left, key)
            elif node.key < key:
                val = find(node.right, key)
            else:
                return node.val
            return val

        return find(self.root, key)

    def getMin(self) -> int:
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        minNode = findMin(self.root)
        if minNode:
            return minNode.val
        else:
            return -1

    def getMax(self) -> int:
        def findMax(root):
            curr = root
            while curr and curr.right:
                curr = curr.right
            return curr

        maxNode = findMax(self.root)
        if maxNode:
            return maxNode.val
        else:
            return -1

    def remove(self, key: int) -> None:
        def minimum(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr

        def remove_tree(node, key):
            if not node:
                return None
            if node.key > key:
                node.left = remove_tree(node.left, key)
            elif node.key < key:
                node.right = remove_tree(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = minimum(node.right)
                    minKey, minVal = minNode.key, minNode.val
                    node.key, node.val = minKey, minVal
                    node.right = remove_tree(node.right, minKey)
            return node

        self.root = remove_tree(self.root, key)

    def getInorderKeys(self) -> List[int]:
        keys = []

        def get_ordered_keys(node):
            if not node:
                return None
            get_ordered_keys(node.left)
            keys.append(node.key)
            get_ordered_keys(node.right)

        get_ordered_keys(self.root)
        return keys
