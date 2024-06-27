/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
export var numWaterBottles = function (numBottles, numExchange) {
  let drank = numBottles;

  while (numBottles >= numExchange) {
    drank += Math.trunc(numBottles / numExchange);
    numBottles =
      Math.trunc(numBottles / numExchange) + (numBottles % numExchange);
  }

  return drank;
};
