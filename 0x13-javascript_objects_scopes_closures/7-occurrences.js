#!/usr/bin/node

let counter;

exports.nbOccurences = function (list, searchElement) {
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      counter++;
    }
  }
  return counter;
};
