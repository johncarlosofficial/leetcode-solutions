/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.next = (next === undefined ? null : next);
 * }
 */

/**
 * LinkedList class to handle operations on linked lists.
 * Contains methods to append new nodes and display the list.
 */
class LinkedList {
  constructor() {
    this.head = null; // Initialize the list with no elements
  }

  /**
   * Appends a list of numbers to the linked list.
   * @param {number[]} nums - A list of integers to be added to the linked list.
   */
  append(nums) {
    nums.forEach((num) => {
      const newNode = new ListNode(num); // Create a new node with the given value

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
    });
  }

  /**
   * Prints out the values in the linked list in a readable format.
   */
  display() {
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
 * Merges two sorted linked lists into one sorted linked list.
 * @param {ListNode} list1 - The head of the first sorted linked list.
 * @param {ListNode} list2 - The head of the second sorted linked list.
 * @return {ListNode} The head of the merged sorted linked list.
 */
var mergeTwoLists = function (list1, list2) {
  // Handle edge cases where one or both lists are empty
  if (!list1 && !list2) {
    return null; // Both lists are empty, return null
  }

  if (!list1) {
    return list2; // Only the first list is empty, return the second list
  }

  if (!list2) {
    return list1; // Only the second list is empty, return the first list
  }

  // Create a dummy node to start the merged list
  let newHead = new ListNode();
  let currentNode = newHead; // This will be used to build the new list

  // Merge the two lists while both have elements
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      currentNode.next = list1; // Attach the smaller node to the merged list
      list1 = list1.next; // Move to the next node in list1
    } else {
      currentNode.next = list2; // Attach the smaller node to the merged list
      list2 = list2.next; // Move to the next node in list2
    }

    currentNode = currentNode.next; // Move to the next position in the merged list
  }

  // If there are remaining nodes in list1, attach them
  if (list1) {
    currentNode.next = list1;
  }

  // If there are remaining nodes in list2, attach them
  if (list2) {
    currentNode.next = list2;
  }

  return newHead.next; // Return the head of the merged list (skipping the dummy node)
};

// Example usage:
const list1 = new LinkedList();
const list2 = new LinkedList();

// Append some values to the linked lists
list1.append([1, 2, 4]);
list2.append([1, 3, 4]);

// Merge the two linked lists and print the result
const mergedListHead = mergeTwoLists(list1.head, list2.head);
const mergedList = new LinkedList();
mergedList.head = mergedListHead;
mergedList.display();
