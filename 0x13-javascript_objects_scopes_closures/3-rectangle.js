#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let row = '';
      for (let l = 0; l < this.width; l++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
