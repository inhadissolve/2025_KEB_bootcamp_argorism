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
            # Case 1: Leaf node
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: Two children
            else:
                min_larger_node = self._find_min(node.right)
                node.data = min_larger_node.data
                node.right = self._delete_node(node.right, min_larger_node.data)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)


# 실행 코드
if __name__ == "__main__":
    bst = BST()
    while True:
        print("1. 삽입")
        print("2. 검색")
        print("3. 삭제")
        print("4. 중위 순회 출력")
        print("5. 종료")
        choice = int(input("메뉴를 선택하세요: "))

        if choice == 1:
            num = int(input("삽입할 숫자를 입력하세요: "))
            bst.insert(num)
        elif choice == 2:
            find_group = int(input("검색할 번호를 입력하세요: "))
            if bst.search(find_group):
                print(f"{find_group}을(를) 찾았습니다")
            else:
                print(f"{find_group}이(가) 존재하지 않습니다")
        elif choice == 3:
            delete_num = int(input("삭제할 번호를 입력하세요: "))
            bst.delete(delete_num)
            print("삭제 완료")
        elif choice == 4:
            print("중위 순회 결과:", end=' ')
            bst.inorder_traversal(bst.root)
            print()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")
