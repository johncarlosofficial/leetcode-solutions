/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  // Calculate the median indices
  let medianIndices = [];
  if ((nums1.length + nums2.length) % 2) {
    // If the total length is odd, there's only one median index
    medianIndices = [Math.floor((nums1.length + nums2.length) / 2)];
  } else {
    // If the total length is even, there are two median indices
    medianIndices = [
      Math.floor((nums1.length + nums2.length) / 2) - 1,
      Math.floor((nums1.length + nums2.length) / 2),
    ];
  }

  // Initialize pointers and current index
  let index1 = 0;
  let index2 = 0;
  let currentIndex = -1;
  let currentMedian = null;

  // Traverse both arrays until reaching the first median index
  while (currentIndex < medianIndices[0]) {
    if (index1 < nums1.length && index2 < nums2.length) {
      if (nums1[index1] <= nums2[index2]) {
        currentMedian = nums1[index1];
        index1++;
      } else {
        currentMedian = nums2[index2];
        index2++;
      }
    } else if (index1 < nums1.length) {
      currentMedian = nums1[index1];
      index1++;
    } else {
      currentMedian = nums2[index2];
      index2++;
    }
    currentIndex++;
  }

  // If there's only one median index, return the current median
  if (medianIndices.length === 1) {
    return currentMedian;
  } else {
    // If there are two median indices, find the next median value
    let secondMedian = null;
    if (index1 < nums1.length && index2 < nums2.length) {
      if (nums1[index1] <= nums2[index2]) {
        secondMedian = nums1[index1];
      } else {
        secondMedian = nums2[index2];
      }
    } else if (index1 < nums1.length) {
      secondMedian = nums1[index1];
    } else {
      secondMedian = nums2[index2];
    }
    // Return the average of the two median values
    return (currentMedian + secondMedian) / 2;
  }
};

// Test case
console.log(findMedianSortedArrays([1, 2], [3, 4]));
