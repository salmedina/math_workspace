class Node():
    def __init__(self, value:int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

class Tree():
    def __init__(self) -> None:
        self.head = None

    def _insert_node(self, node:Node, value:int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_node(node.left, value)
        if value >= node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_node(node.right, value)

    def insert(self, value:int) -> None:
        if self.head is None:
            self.head = Node(value)
        else:
            self._insert_node(self.head, value)

    def calc_height(self):
        def _calc_height(node:Node) -> int:
            if node is None:
                return 0

            l_height = _calc_height(node.left)
            r_height = _calc_height(node.right)

            return max(l_height, r_height) + 1

        if self.head is None:
            return 0

        return _calc_height(self.head)

def print_dfs(tree:Tree) -> None:
    def _print_dfs(node:Node):
        if node is None:
            return
        print(node.value, end=' ')
        print(' <- ')
        _print_dfs(node.left)
        print(' -> ')
        _print_dfs(node.right)
        print(' ^ ')

    if tree is None:
        return

    if tree.head is None:
        return

    _print_dfs(tree.head)

def print_bfs(tree:Tree) -> None:

    def _print_bfs(node:None, level:int) -> bool:
        printed_something = False
        level -= 1
        if level == 0:
            if node.left is not None:
                print(node.left.value, end=' ')
                printed_something = True
            if node.right is not None:
                print(node.right.value, end=' ')
                printed_something = True

        if node.left is not None:
            _print_bfs(node.left, level)
        if node.right is not None:
            _print_bfs(node.right, level)
            
        return printed_something

    if tree is None:
        return
    if tree.head is None:
        return
    
    height = tree.calc_height()
    print(tree.head.value)
    for level in range(1, height + 1):
        _print_bfs(tree.head, level)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(10)
    tree.insert(7)

    print_bfs(tree)