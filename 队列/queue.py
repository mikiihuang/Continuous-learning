class Queue(object):
    def __init__(self):
        self.items =[]
    def is_empty(self):
        return self.items == []
    def enqueue(self,elem):
        # 队列添加元素
        self.items.insert(0,elem)
    def dequeue(self):
        # 从队列头部删除一个元素
        return self.items.pop()
    def size(self):
        return len(self.items)
if __name__ == '__main__':
    queue = Queue()
    print("======判断队列是否为空==========")
    print(queue.is_empty())
    print("======队列加入元素==========")
    queue.enqueue(2)
    queue.enqueue("hello")
    queue.enqueue("end")

    print("队列的长度为：", queue.size())
    print("======判断队列是否为空==========")
    print(queue.is_empty())
    print("======返回队列头部元素==========")
    print(queue.dequeue())

    print("队列的长度为：",queue.size())