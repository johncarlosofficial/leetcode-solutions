var TimeMap = function () {
  // Initialize the dictionary
  this.hashMap = {};
};

/**
 * @param {string} key
 * @param {string} value
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function (key, value, timestamp) {
  // Add value and timestamp to the key
  if (!this.hashMap[key]) {
    this.hashMap[key] = [];
  }
  this.hashMap[key].push([value, timestamp]);
};

/**
 * @param {string} key
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function (key, timestamp) {
  // Return empty string if key is not found
  if (!this.hashMap[key]) {
    return "";
  }

  const values = this.hashMap[key];
  let left = 0;
  let right = values.length - 1;

  // Binary search for the closest timestamp <= given timestamp
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (values[mid][1] === timestamp) {
      return values[mid][0];
    } else if (values[mid][1] < timestamp) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  // Return the value with the closest timestamp <= given timestamp
  return right >= 0 ? values[right][0] : "";
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key, value, timestamp)
 * var param_2 = obj.get(key, timestamp)
 */
