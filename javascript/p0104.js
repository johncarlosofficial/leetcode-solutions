/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  // If the tree is empty (root is None), the depth is 0
  if (!root) return 0;

  // Recursively find the maximum depth of the left and right subtrees.
  // Add 1 to account for the current node.
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
  // The max function returns the larger of the two depths (left or right),
  // and adding 1 includes the current node in the depth count.
};
