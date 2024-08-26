/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  // Base case: If the tree is empty (root is null), return null
  if (!root) return null;

  // Store the left and right child nodes temporarily
  let left = root.left;
  let right = root.right;

  // Swap the left and right child nodes
  root.left = right;
  root.right = left;

  // Recursively invert the left subtree (which was originally the right subtree)
  invertTree(right);
  // Recursively invert the right subtree (which was originally the left subtree)
  invertTree(left);

  // Return the root node, which now represents the inverted tree
  return root;
};
