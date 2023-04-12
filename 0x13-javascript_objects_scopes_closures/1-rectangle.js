#!/usr/bin/node

// a class rectangle
// module.exports is an obj that holds exported values and
// functions from that module

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
