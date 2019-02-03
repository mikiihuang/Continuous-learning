
class Node(object):
    def __init__(self,item):
        self.item = item
        self._next = None



class singleLinkList(object):
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
        # 首先要指向头节点
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur._next
        print("")
    def first_add(self,elem):
        # 把新添加的数定义到Node类里，这样它就会有item和_next两个属性
        p = Node(elem)
        p._next = self._head
        # 把链表的头节点指向新添加的节点
        self._head = p

    def last_add(self,elem):
        cur = self._head
        p = Node(elem)
        # 首先判断这个链表是不是空的
        if self.is_empty():
            self._head = p
        else:
            cur = self._head
            while cur != None:
                cur = cur._next
            cur._next = p
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
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == elem:
                #  如果第一个就是要删除的节点
                if not pre:
                    self._head = cur._next
                else:
                    pre._next = cur._next
                break
            else:
                cur = cur._next
                pre = pre._next
    def search(self,elem):
        cur = self._head
        index = 0
        while cur is not None:
            if cur.item == elem:
                return index
            else:
                cur = cur._next
                index = index+1
        return index
if __name__ == "__main__":
    ll = singleLinkList()

    ll.first_add(1)
    # print(ll.travel())
    ll.first_add(2)
    print(ll.travel())
    ll.last_add(3)
    # print(ll.travel())
    # ll.insert(2, 4)
    # print("length:",ll.length())
    # ll.travel()
    # print ll.search(3)
    # print ll.search(5)
    # ll.remove(1)
    # print "length:",ll.length()
    # ll.travel()

