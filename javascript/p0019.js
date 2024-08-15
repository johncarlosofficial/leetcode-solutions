class ListNode {
  // Represents a node in the linked list, holding a value and a reference to the next node
  constructor(value = 0, nextNode = null) {
    this.val = value;
    this.next = nextNode;
  }
}

class LinkedList {
  // Initializes an empty linked list with head and tail pointers
  constructor() {
    this.head = null;
    this.tail = null;
  }

  // Adds nodes to the linked list from an array of integers
  addNodes(values) {
    for (let i = 0; i < values.length; i++) {
      if (!this.head) {
        // If the list is empty, set the first node as both head and tail
        this.head = new ListNode(values[i]);
        this.tail = this.head;
      } else {
        // Add new node at the end and update the tail reference
        this.tail.next = new ListNode(values[i]);
        this.tail = this.tail.next;
      }
    }
  }

  // Displays the linked list in a readable format
  display() {
    let currentNode = this.head;
    let output = "";
    while (currentNode) {
      output += `${currentNode.val} -> `;
      currentNode = currentNode.next;
    }
    console.log(output + "None");
  }
}

// Function to remove the nth node from the end of the linked list
var removeNthFromEnd = function (head, n) {
  if (!head) {
    return null;
  }

  // Dummy node helps to simplify edge cases (like removing the first node)
  let dummyNode = new ListNode();
  dummyNode.next = head;

  // Initialize two pointers, both starting from the dummy node
  let slow = dummyNode;
  let fast = dummyNode;

  // Move the 'fast' pointer n steps ahead
  for (let i = 0; i < n; i++) {
    fast = fast.next;
  }

  // Move both pointers until 'fast' reaches the last node
  while (fast.next) {
    slow = slow.next;
    fast = fast.next;
  }

  // 'slow.next' is the node to be removed; skip it
  slow.next = slow.next.next;

  // Return the head of the updated list
  return dummyNode.next;
};

// Case usage
let linkedList = new LinkedList();
linkedList.addNodes([1, 2, 3, 4, 5]);
linkedList.addNodes([6, 7, 8]);
linkedList.display();

removeNthFromEnd(linkedList.head, 3);
linkedList.display();
