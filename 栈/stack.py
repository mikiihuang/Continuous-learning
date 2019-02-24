class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        # 判断栈是否为空
        return self.items == []
    def push(self,elem):
        # 添加元素到栈
        self.items.append(elem)
    def pop(self):
        # 弹出元素
        return self.items.pop()
    def peek(self):
        # 返回栈顶的元素
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def travel(self):
        for i in range(self.size()):
            print(self.items[i],end=" ")
if __name__ == '__main__':
    stack = Stack()
    print(stack.travel())
    print("======判断栈是否为空==========")
    print(stack.is_empty())
    print("======栈顶加入元素==========")
    stack.push(2)
    stack.push(3)
    stack.push(12)
    stack.push(4)
    print(stack.travel())
    print("栈的长度为：", stack.size())
    print("======判断栈是否为空==========")
    print(stack.is_empty())
    print("======弹出栈顶元素==========")
    print(stack.pop())
    print("======返回栈顶元素==========")
    print(stack.peek())
    print("栈的长度为：",stack.size())