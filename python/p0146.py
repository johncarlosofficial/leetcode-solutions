class Node:
    def __init__(self, key, value):
        self.key = key            # Store the key for the cache entry
        self.value = value        # Store the value for the cache entry
        self.prev = None          # Pointer to the previous node in the linked list
        self.next = None          # Pointer to the next node in the linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum number of entries the cache can hold
        self.cache = {}           # Dictionary to store key-node pairs for O(1) access
        self.head = Node(0, 0)    # Dummy head node to simplify operations
        self.tail = Node(0, 0)    # Dummy tail node to simplify operations
        self.head.next = self.tail # Initialize the linked list as empty
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev = node.prev          # Get the previous node
        next = node.next          # Get the next node
        prev.next = next          # Bypass the current node
        next.prev = prev          # Bypass the current node

    def _add(self, node: Node):
        """Add a node right before the tail (marking it as most recently used)."""
        prev = self.tail.prev     # Get the node currently at the tail's previous position
        prev.next = node          # Insert the new node after the previous tail node
        node.prev = prev          # Set the new node's previous pointer
        node.next = self.tail     # Point the new node's next to the tail
        self.tail.prev = node     # Update the tail's previous pointer

    def get(self, key: int) -> int:
        if key in self.cache:     # If the key is in the cache
            node = self.cache[key] # Retrieve the node
            self._remove(node)    # Remove the node from its current position
            self._add(node)       # Add it back to the end to mark it as recently used
            return node.value     # Return the value associated with the key
        return -1                 # Return -1 if the key is not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:     # If the key is already in the cache
            node = self.cache[key] # Retrieve the node
            node.value = value    # Update its value
            self._remove(node)    # Remove the node from its current position
            self._add(node)       # Add it back to the end to mark it as recently used
        else:
            if len(self.cache) >= self.capacity: # If the cache is full
                lru = self.head.next # The node after the head is the least recently used
                self._remove(lru)    # Remove the least recently used node
                del self.cache[lru.key] # Remove the key from the cache dictionary
            new_node = Node(key, value) # Create a new node for the key-value pair
            self.cache[key] = new_node # Add the new node to the cache dictionary
            self._add(new_node)        # Add the new node to the end of the linked list

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
