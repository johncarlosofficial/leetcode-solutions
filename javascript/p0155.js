var MinStack = function () {
  this.stack = []; // Main stack to store elements
  this.min = []; // Stack to keep track of minimums
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
  this.stack.push(val);
  // Update min stack if necessary
  if (this.min.length === 0 || val <= this.min[this.min.length - 1]) {
    this.min.push(val);
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  if (this.stack) {
    // Remove from min stack if it's the min value
    if (this.stack[this.stack.length - 1] === this.min[this.min.length - 1]) {
      this.min.pop();
    }
    this.stack.pop();
  }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  if (this.stack) {
    return this.stack[this.stack.length - 1]; // Return top element of the main stack
  }
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  if (this.min) {
    return this.min[this.min.length - 1]; // Return the current minimum
  }
};

/**
 * Example usage:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
