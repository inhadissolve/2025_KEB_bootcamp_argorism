from collections import deque

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

root = TreeNode()
root.data = 10
root.left = TreeNode()
root.left.data = 5
root.right = TreeNode()
root.right.data = 15

queue = deque([root])
current = queue.popleft()  # 루트 노드(10)를 가져옴
print(current.data)  # 10


