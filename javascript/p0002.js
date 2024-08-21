// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  // Initialize a dummy node to keep track of the result's head
  let dummy = new ListNode();
  // 'current' points to the last node in the result list
  let current = dummy;

  let carry = 0; // To store carry from the previous digit sum

  // Loop through both lists as long as both have nodes
  while (l1 !== null && l2 !== null) {
    // Calculate the sum of current digits plus carry
    let currentSum = l1.val + l2.val + carry;
    // The new digit to add to the result list is the sum modulo 10
    let newDigit = currentSum % 10;
    // Update carry for the next iteration
    carry = Math.floor(currentSum / 10);

    // Add the new digit to the result list
    current.next = new ListNode(newDigit);
    current = current.next; // Move to the next node in the result list

    // Move to the next nodes in l1 and l2
    l1 = l1.next;
    l2 = l2.next;
  }

  // If list1 is longer, continue adding its remaining digits
  while (l1 !== null) {
    let currentSum = l1.val + carry;
    let newDigit = currentSum % 10;
    carry = Math.floor(currentSum / 10);

    current.next = new ListNode(newDigit);
    current = current.next;

    l1 = l1.next;
  }

  // If list2 is longer, continue adding its remaining digits
  while (l2 !== null) {
    let currentSum = l2.val + carry;
    let newDigit = currentSum % 10;
    carry = Math.floor(currentSum / 10);

    current.next = new ListNode(newDigit);
    current = current.next;

    l2 = l2.next;
  }

  // If there's any carry left after processing both lists, add it as a new digit
  if (carry !== 0) {
    current.next = new ListNode(carry);
  }

  // Return the result list, starting from the node after dummy
  return dummy.next;
};
