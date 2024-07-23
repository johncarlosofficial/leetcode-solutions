/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  // Stack to keep track of temperatures and their indices
  let tempStack = [];
  // Answer list initialized with zeros, same length as temperatures list
  let daysToWait = new Array(temperatures.length).fill(0);

  for (let currentDay = 0; currentDay < temperatures.length; currentDay++) {
    let currentTemp = temperatures[currentDay];
    // Check if the current temperature is higher than the temperature at the top of the stack
    while (
      tempStack.length > 0 &&
      currentTemp > tempStack[tempStack.length - 1][0]
    ) {
      // Pop the top element from the stack (it's now warmer)
      let [previousTemp, previousDay] = tempStack.pop();
      // Calculate the number of days to wait for a warmer temperature
      daysToWait[previousDay] = currentDay - previousDay;
    }
    // Push the current temperature and its index onto the stack
    tempStack.push([currentTemp, currentDay]);
  }

  return daysToWait;
};

console.log(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]));
