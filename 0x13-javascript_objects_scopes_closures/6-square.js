#!/usr/bin/node

const SquareToo = require('./5-square');

module.exports = class Square extends SquareToo {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
