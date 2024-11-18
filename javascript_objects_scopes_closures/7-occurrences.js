#!/usr/bin/node
/**
 * Counts the number of occurrences of a specific element in a list.
 *
 * @param {Array} list - The list to search.
 * @param {*} searchElement - The element to count in the list.
 * @returns {number} The number of occurrences of searchElement in the list.
 */
exports.nbOccurences = function (list, searchElement) {
    return list.filter(item => item === searchElement).length;
  };
  