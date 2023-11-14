#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let square = '';
    for (let i = this.height; i > 0; i--) {
      for (let j = this.width; j > 0; j--) {
        square += 'X';
      }
      if (i > 1) {
        square += '\n';
      }
    }
    if (square) {
      console.log(square);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}
module.exports = Rectangle;
