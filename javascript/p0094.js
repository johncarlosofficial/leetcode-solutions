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
 * @return {number[]}
 */
var inorderTraversal = function (root) {
  let result = [];

  function traverse(node) {
    if (!node) return;
    // Traverse the left subtree
    traverse(node.left);
    // Visit the root node
    result.push(node.val);
    // Traverse the right subtree
    traverse(node.right);
  }

  // Start the traversal from the root node
  traverse(root);

  return result;
};
