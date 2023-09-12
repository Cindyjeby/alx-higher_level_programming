#!usr/bin/node

const Rectangle = require('./rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
