class DoubleQueue(object):
    """
    Deque() 创建一个空的双端队列
    add_front(item) 从队头加入一个item元素
    add_rear(item) 从队尾加入一个item元素
    remove_front() 从队头删除一个item元素
    remove_rear() 从队尾删除一个item元素
    is_empty() 判断双端队列是否为空
    size() 返回队列的大小
    """
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self,elem):
        # 从队头加入一个元素
        self.items.insert(0,elem)
    def add_rear(self,elem):
        # 队尾加入一个元素
        self.items.append(elem)
    def remove_front(self):
        # 队头删除一个元素
        return self.items.pop(0)
    def remove_rear(self):
        # 队尾删除一个元素
        return self.items.pop()
    def size(self):
        return len(self.items)
    def travel(self):
        for i in range(self.size()):
            print(self.items[i],end=" ")
if __name__ == '__main__':
    deque = DoubleQueue()
    print("======判断双端队列是否为空==========")
    print(deque.is_empty())
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print("======双端队列的值为:==========")
    deque.travel()
    print("双端队列的长度为:",deque.size())
    print("======队头删除的元素==========")
    print(deque.remove_front())
    print("======队尾删除的元素==========")
    print(deque.remove_rear())
    print("双端队列的长度为:", deque.size())



