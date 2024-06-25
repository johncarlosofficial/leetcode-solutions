/**
 * @param {string[]} strs
 * @return {string[][]}
 */
export var groupAnagrams = function (strs) {
  let groups = {};

  for (let i = 0; i < strs.length; i++) {
    let temp = [];

    for (let j = 0; j < strs[i].length; j++) {
      temp.push(strs[i][j]);
    }

    temp.sort();

    temp = temp.join("");

    if (temp in groups) {
      groups[temp].push(strs[i]);
    } else {
      groups[temp] = [strs[i]];
    }
  }

  return Object.values(groups);
};
