class Stack:
    def __init__(self):
        self.items = list()

    def push(self, data) -> object:
        self.items.append(data)

    def pop(self) -> object:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> object:
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(977)
print(s1.pop())
print(s1.peek())
print(s1.peek())
# print(s1.pop())
# print(s1.pop())
print(s1.is_empty())