"""
Clarifying questions:
1. what is the maximum size of the cache? should the cache size be fixed or dynamic?
2. what is the key and value data Type?should I assume integer for simplicity?
3. should the cache support get and put? Do I need to get it O(1) time complexity?
4. what is the evication policy? should the cache evict the least recently used item when full?

Approach
Data Structures:

Doubly Linked List: to keep track of the order of items. 
The most recently used (MRU) items will be close to the right dummy node (tail), 
and the least recently used (LRU) items will be close to the left dummy node (head).

HashMap (Dictionary): map keys to their corresponding nodes in the doubly linked list.
This allows for O(1) access to nodes for both retrieval and update operations."""


class Node:  # Holds the key, value, and pointers (prev and next) for the doubly linked list.
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # map key to node and quick look up

        # left = LRU right= MRU
        self.left = Node(0, 0)  # dummy head
        self.right = Node(0, 0)  # dmmy tail
        self.left.next = self.right
        self.right.prev = self.left

        # pointer function

    def remove(self, node):
        prev = node.prev
        nxt_node = node.next
        prev.next = nxt_node
        nxt_node.prev = prev

    def insert(self, node):  # Inserts a node right before the dummy tail node
        prev = self.right.prev
        nxt_node = self.right

        prev.next = nxt_node.prev = node
        node.next = nxt_node
        node.prev = prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


def test_lru_cache():
    # Test 1: Basic functionality
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Cache is {2=2, 1=1}
    cache.put(3, 3)  # Evicts key 2, Cache is {1=1, 3=3}
    assert cache.get(2) == -1  # Key 2 was evicted
    cache.put(4, 4)  # Evicts key 1, Cache is {3=3, 4=4}
    assert cache.get(1) == -1  # Key 1 was evicted
    assert cache.get(3) == 3  # Cache is {4=4, 3=3}
    assert cache.get(4) == 4  # Cache is {3=3, 4=4}

    # Test 2: Updating existing key
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(2, 20)  # Update key 2
    assert cache.get(2) == 20  # Key 2 should have updated value
    cache.put(3, 3)  # Evicts key 1, Cache is {2=20, 3=3}
    assert cache.get(1) == -1  # Key 1 was evicted
    assert cache.get(2) == 20  # Cache is {3=3, 2=20}

    # Test 3: Capacity 1
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1  # Cache is {1=1}
    cache.put(2, 2)  # Evicts key 1, Cache is {2=2}
    assert cache.get(1) == -1  # Key 1 was evicted
    assert cache.get(2) == 2  # Cache is {2=2}

    # Test 4: Edge case - empty cache
    cache = LRUCache(0)
    cache.put(1, 1)  # Should not store anything
    assert cache.get(1) == -1  # Cache should be empty

    print("All tests passed.")


print(test_lru_cache())
