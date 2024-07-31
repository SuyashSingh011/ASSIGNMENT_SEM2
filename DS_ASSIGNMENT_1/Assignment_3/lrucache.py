class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Key -> Node
        self.head = Node(0, 0) 
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head

    # Move a node to the front (right after the head)
    def __move_to_front(self, node):
        self.__remove(node)
        self.__add(node)

    # Remove a node from the linked list
    def __remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Add a node right after the head
    def __add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
 
    # Remove the least recently used node
    def __remove_lru(self):
        lru = self.tail.prev
        self.__remove(lru)
        del self.cache[lru.key]

    #  Getting the value of the key if the key exists, otherwise we will return -1
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.__move_to_front(node)  # Move the accessed node to the front
            return node.value
        return -1

    # Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
    # If the number of keys exceeds the capacity, remove the least recently used key.
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.__move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                self.__remove_lru()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.__add(new_node)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Return 1
cache.put(3, 3)      # remove key 2
print(cache.get(2))  # Return -1 (not found)
cache.put(4, 4)      # remove key 1
print(cache.get(1))  # Return -1 (not found)
print(cache.get(3))  # Return 3
print(cache.get(4))  # Return 4
