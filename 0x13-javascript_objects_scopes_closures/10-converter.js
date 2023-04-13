#!/usr/bin/node

exports.converter = function (base) {
  function conversion (num) {
    return num.toString(base);
  }
  return (conversion);
};
