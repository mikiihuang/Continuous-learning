
class Node(object):
    def __init__(self,item):
        self.item = item
        self._next = None



class circularLinkList(object):
    def __init__(self):
        # 头节点
        self._head = None
    def is_empty(self):
        return self._head == None

    def length(self):
        # 首先要指向头节点
        cur = self._head
        count = 0
        while cur is not None:
            count = count+1
            cur = cur._next
        return count


    def travel(self):
        if self.is_empty():
            return
        # 首先要指向头节点
        cur = self._head

        while cur._next != self._head:
            print(cur.item)
            cur = cur._next
        print(cur.item)
        print("")


    def first_add(self,elem):
        # 把新添加的数定义到Node类里，这样它就会有item和_next两个属性
        p = Node(elem)
        if self.is_empty():
            self._head = p
            p._next = self._head
        else:
            # 首先将新加入的这个节点的下一个节点指向首节点
            p._next = self._head
            # 然后将原链表的尾节点指向这个新加入的节点
            cur = self._head
            while cur._next != self._head:
                cur = cur._next
            cur._next = p
            self._head = p


    def last_add(self,elem):

        p = Node(elem)
        # 首先判断这个链表是不是空的
        if self.is_empty():
            self._head = p
            p._next = self._head
        else:
            # 直接走到最后的节点
            cur = self._head
            while cur._next != self._head:
                cur = cur._next
            cur._next = p
            p._next = self._head



    def insert(self,index,elem):
        # 如果插入的地方在第一个位置之前，直接调用在首部插入的方法
        if index<=0 :
            self.first_add(elem)
        # 如果插入的地方在最后一个位置之后，直接调用在尾部插入的方法
        elif index>(self.length()-1):
            self.last_add(elem)
        else:
            p = Node(elem)
            count = 0
            pre = self._head
            while count<(index-1):
                pre = pre._next
                count = count+1
            p._next = pre._next
            pre._next = p

    def remove(self,elem):
        # 如果原链表为空
        if self.is_empty():
            return

        cur = self._head
        pre = None

        # 如果链表的第一个元素就是要删除的元素
        if cur.item == elem:
            # 如果链表多于一个节点，就找到最后一个节点
            if cur._next != self._head:
                while cur._next != self._head:
                    cur = cur._next
                cur._next = self._head._next
                self._head = self._head._next
            else:
                # 如果链表只有一个元素，就直接置空
                self._head = None
        else:
            pre = self._head
            while cur._next != self._head:
                # 如果找到了要找的元素
                if cur.item == elem:
                    pre._next = cur._next
                    return
                else:
                    pre = cur
                    cur = cur._next
            # cur指向了尾节点
            if cur.item == elem:
                pre._next = self._head



    def search(self,elem):
        if self.is_empty():
            return False
        cur = self._head
        index = 0
        while cur._next != self._head:
            if cur.item == elem:
                return index
            else:
                cur = cur._next
                index = index+1
        if cur.item == elem:
            return index
        else:
            return False

if __name__ == "__main__":
    ll = circularLinkList()
    # print(ll.length())
    ll.travel()
    print("--------首部添加----------")
    ll.first_add(2)
    ll.first_add(1)
    ll.first_add(99)
    ll.travel()
    print("--------尾部添加----------")
    ll.last_add(6)
    ll.travel()
    print("--------尾部添加----------")
    ll.last_add(5)
    ll.travel()
    print("--------移除元素----------")
    # ll.remove(5)
    # ll.travel()
    print("--------查找元素----------")
    print(ll.search(6))
