// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * Reverses a singly-linked list.
 * @param {ListNode} head - The head of the singly-linked list.
 * @return {ListNode} - The new head of the reversed list.
 */
var reverseList = function (head) {
  let prev_node = null;
  let cur_node = head;

  while (cur_node) {
    let next_node = cur_node.next; // Save reference to the next node
    cur_node.next = prev_node; // Reverse the current node's pointer
    prev_node = cur_node; // Move prev_node to the current node
    cur_node = next_node; // Move to the next node
  }

  return prev_node; // Return the new head of the reversed list
};

// Example usage:
// Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> null
let node1 = new ListNode(1);
let node2 = new ListNode(2);
let node3 = new ListNode(3);
let node4 = new ListNode(4);
let node5 = new ListNode(5);

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

// Before reversal, the list is: 1 -> 2 -> 3 -> 4 -> 5 -> null
let reversedHead = reverseList(node1);

// After reversal, the list should be: 5 -> 4 -> 3 -> 2 -> 1 -> null
// Let's print the reversed list to verify
let current = reversedHead;
while (current) {
  process.stdout.write(current.val + (current.next ? " -> " : " -> null\n"));
  current = current.next;
}
