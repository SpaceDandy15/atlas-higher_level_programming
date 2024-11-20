#!/usr/bin/node
/**
 * Function to reverse a list without using the built-in reverse method.
 * @param {Array} list - The array to reverse.
 * @returns {Array} - The reversed array.
 */
exports.esrever = function (list) {
    const reversedList = [];
    for (let i = list.length - 1; i >= 0; i--) {
      reversedList.push(list[i]);
    }
    return reversedList;
  };
  