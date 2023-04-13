#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// a class square
// inherits from the class Rectangle
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
