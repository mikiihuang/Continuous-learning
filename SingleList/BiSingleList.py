

# 双向链表，不是循环双向链表
class Node(object):
    def __init__(self,item):
        self.item = item
        self._next = None
        self._prev = None

class BiSingleList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur._next is not None:
            count = count+1
            cur = cur._next
        count +=1
        return count


    def travel(self):
        cur = self._head
        if cur is None:
            return ""
        else:
            while cur is not None:
                print(cur.item,end=" ")
                cur = cur._next



    def first_add(self,elem):
        # 链表头部添加元素
        node = Node(elem)

        if self.is_empty():
            self._head = node
        else:
            node._next = self._head
            self._head._prev = node
            self._head = node

    def last_add(self,elem):
        #  尾部插入元素
        node = Node(elem)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur._next is not None:
                cur = cur._next
            cur._next = node
            node._prev = cur

    def insert(self,index,elem):
        if index <= 0 :
            self.first_add(elem)
        elif index > self.length():
            self.last_add(elem)
        else:
            cur = self._head
            node = Node(elem)
            pre_count = 0
            while pre_count<index:
                cur = cur._next
                pre_count +=1
            node._next = cur._next
            node._prev = cur
            cur._next = node
            cur._next._prev = node

    def remove(self,elem):
        if self.is_empty():
            return
        else:
            cur = self._head

            if cur.item == elem:
                # 链表只有一个元素，且这个元素等于要删除的数
                if cur._next is None:
                    self._head = None
                else:
                    # 链表不止一个元素，但第一个元素就是要删除的数
                    self._head = cur._next
                    cur._next._prev = None
            else:
                while cur is not None:
                    if cur._next is not None:
                        cur = cur._next
                        if cur.item == elem:
                            cur._prev._next = cur._next
                            cur._next._prev = cur._prev
                            break
                    else:
                        if cur.item == elem:
                            cur._prev._next = None

                # if cur is None:







if __name__ == '__main__':
     ll = BiSingleList()
     ll.travel()
     ll.first_add(2)
     ll.first_add(3)
     ll.last_add(4)
     ll.travel()
     print("\n")
     ll.insert(9,7)
     ll.travel()
     print("\n")
     ll.remove(7)
     ll.travel()


