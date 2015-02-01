#! /usr/bin/python

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.l = 0
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}

    # @return an integer
    def get(self, key):
        if key in self.d:
            
            self.d[key].prev.next = self.d[key].next
            self.d[key].next.prev = self.d[key].prev
            
            self.tail.prev.next = self.d[key]
            self.d[key].prev = self.tail.prev
            self.d[key].next = self.tail
            self.tail.prev = self.d[key]
            return self.d[key].val
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.d:
            if self.d[key].next != self.tail:
                self.d[key].val = value
                self.d[key].prev.next = self.d[key].next
                self.d[key].next.prev = self.d[key].prev
                self.tail.prev.next = self.d[key]
                self.d[key].prev = self.tail.prev
                self.d[key].next = self.tail
                self.tail.prev = self.d[key]
            else:
                self.d[key].val = value
        else:
            if self.l < self.cap:
                self.d[key] = ListNode(key, value)
                self.tail.prev.next = self.d[key]
                self.d[key].prev = self.tail.prev
                self.d[key].next = self.tail
                self.tail.prev = self.d[key]
                self. l += 1
            else:
                temp1 = self.head.next
                
                temp2 = self.head.next.next
                self.head.next = temp2
                temp2.prev = self.head
                del self.d[temp1.k]
                
                self.d[key] = ListNode(key, value)
                self.tail.prev.next = self.d[key]
                self.d[key].prev = self.tail.prev
                self.d[key].next = self.tail
                self.tail.prev = self.d[key]
            
            
            
        
        
class ListNode:
    #Doubly linked list
    def __init__(self, key, value):
        self.val = value
        self.k = key
        self.next = None
        self.prev = None

if __name__ == "__main__":
    cache = LRUCache(2)
    print cache.d
    cache.set(2,1)
    cache.set(1,1)
    print cache.d
    print cache.get(2)
    print cache.d
    cache.set(4,1)
    print cache.d
    print cache.get(1)
    print cache.get(2)
    print cache.d
