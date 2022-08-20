class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetoHead(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.addtoHead(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                removedNode = self.removeTail()
                self.cache.pop(removedNode.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.movetoHead(node)

    def addtoHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        # node.prev = self.head
        # node.next = self.head.next
        # self.head.next.prev = node
        # self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def movetoHead(self, node):
        self.removeNode(node)
        self.addtoHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


if __name__ == '__main__':
    obj = LRUCache(capacity=2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
