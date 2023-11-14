#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let square = '';
    const char = c || 'X';
    for (let i = this.height; i > 0; i--) {
      for (let j = this.width; j > 0; j--) {
        square += char;
      }
      if (i > 1) {
        square += '\n';
      }
    }
    if (square) {
      console.log(square);
    }
  }
}
module.exports = Square