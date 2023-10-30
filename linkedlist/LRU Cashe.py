class Node:
    def __init__(self,key,val):
        self.key =key
        self.val =val
        self.prev = None
        self.next = None
class LRUCashe:
    def __init__(self,capacity):
        self.cap= capacity
        self.cash ={} # map key to node


        # left = LRU right= MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left


        # pointer function
    def remove(self,node):
        prev = node.prev
        nxt_node = node.next
        prev.next = nxt_node
        nxt_node.prev = prev



    def insert(self,node):
        prev= self.right.prev
        nxt_node = self.right

        prev.next = nxt_node.prev = node
        node.next =nxt_node
        node.prev= prev
        



    def get(self,key):
        if key in self.cache:
            self.remove(self.cash[key])
            self.insert(self.cash[key])

            return self.cash[key].val
        return -1


    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cash[key])
        self.cash[key]= Node(key,value)
        self.insert(self.cash[key])

        if len(self.cash)> self.cap:
            # remove the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cash[lru.key]