/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.next = (next === undefined ? null : next);
 * }
 */

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

class LinkedList {
  constructor() {
    this.head = null; // Initialize the list with no elements
  }

  append(nums) {
    // Appends a list of numbers to the linked list
    for (let num of nums) {
      let newNode = new ListNode(num); // Create a new node with the given value

      if (!this.head) {
        // If the list is empty, set the new node as the head
        this.head = newNode;
      } else {
        let currentNode = this.head; // Start at the head of the list

        // Traverse the list to find the last node
        while (currentNode.next) {
          currentNode = currentNode.next;
        }

        // Attach the new node to the end of the list
        currentNode.next = newNode;
      }
    }
  }

  display() {
    // Prints out the values in the linked list in a readable format
    let currentNode = this.head; // Start at the head of the list

    // Traverse the list and print each value
    while (currentNode) {
      process.stdout.write(currentNode.val + " -> ");
      currentNode = currentNode.next;
    }

    console.log("None"); // Indicate the end of the list
  }
}

/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  // 1. Find the middle of the list using two pointers (slow and fast)
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next; // Move slow pointer by one step
    fast = fast.next.next; // Move fast pointer by two steps
  }

  // 2. Split the list into two halves
  let rightHead = slow.next; // Start of the second half
  slow.next = null; // End the first half

  // 3. Reverse the second half of the list
  let prevNode = null;
  let currNode = rightHead;

  while (currNode !== null) {
    let nextNode = currNode.next; // Store the next node
    currNode.next = prevNode; // Reverse the link
    prevNode = currNode; // Move prevNode to current node
    currNode = nextNode; // Move currNode to next node
  }

  rightHead = prevNode; // rightHead now points to the reversed list

  // 4. Merge the two halves, alternating nodes from each half
  let leftHead = head; // Pointer to the start of the first half

  // Temporary node to facilitate merging
  let currNodeDummy = new ListNode();

  while (leftHead !== null && rightHead !== null) {
    let nextLeftHead = leftHead.next;
    let nextRightHead = rightHead.next;

    currNodeDummy.next = leftHead;
    currNodeDummy = currNodeDummy.next;

    currNodeDummy.next = rightHead;
    currNodeDummy = currNodeDummy.next;

    leftHead = nextLeftHead;
    rightHead = nextRightHead;
  }

  // If there are any remaining nodes in the first or second half, append them
  if (leftHead !== null) {
    currNodeDummy.next = leftHead;
  }
  if (rightHead !== null) {
    currNodeDummy.next = rightHead;
  }
};

// Example usage:
let list1 = new LinkedList();

// Append some values to the linked list
list1.append([1, 2, 3, 4, 5]);

// Display the original list
console.log("Original List:");
list1.display();

// Reorder the list
reorderList(list1.head);

// Display the reordered list
console.log("Reordered List:");
list1.display();
