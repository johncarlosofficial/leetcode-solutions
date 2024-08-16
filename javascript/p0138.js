/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  // Return null if the list is empty.
  if (!head) return null;

  // Map original Nodes to their copies.
  const originalToCopy = new Map();
  originalToCopy.set(null, null);

  // Create copies of all Nodes.
  let cur = head;
  while (cur) {
    originalToCopy.set(cur, new _Node(cur.val));
    cur = cur.next;
  }

  // Set next and random pointers.
  cur = head;
  while (cur) {
    const copy = originalToCopy.get(cur);
    copy.next = originalToCopy.get(cur.next);
    copy.random = originalToCopy.get(cur.random);
    cur = cur.next;
  }

  // Return the copied list's head.
  return originalToCopy.get(head);
};
