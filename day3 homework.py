class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, data):
        self.root = self._delete_node(self.root, data)

    def _delete_node(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            # Case 1: 리프노드(자식없음)
            if node.left is None and node.right is None:
                return None
            # Case 2: 자식 1개
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: 자식 2개
            else:
                min_larger_node = self._find_min(node.right)
                node.data = min_larger_node.data
                node.right = self._delete_node(node.right, min_larger_node.data)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def result(self, node):
        if node:
            self.result(node.left)
            print(node.data, end=' ')
            self.result(node.right)


# 실행 코드
if __name__ == "__main__":
    bst = BST()
    numbers = [10, 15, 8, 3, 9]
    for num in numbers:
        bst.insert(num)

    print("BST 구성 완료")
    print("중위 순회 결과:", end=' ')
    bst.result(bst.root)
    print()

    insert_num = int(input("삽입할 번호를 입력하세요: "))
    bst.insert(insert_num)
    print("삽입 후 중위 순회 결과:", end=' ')
    bst.result(bst.root)
    print()

    find_group = int(input("검색할 번호를 입력하세요: "))
    if bst.search(find_group):
        print(f"{find_group}을(를) 찾았습니다")
    else:
        print(f"{find_group}이(가) 존재하지 않습니다")

    delete_num = int(input("삭제할 번호를 입력하세요: "))
    bst.delete(delete_num)
    print("삭제 후 중위 순회 결과:", end=' ')
    bst.result(bst.root)
    print()