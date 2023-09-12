#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;

  for (let k = 0; k < list.lenght; k++) {
    if (searchElement === list[k]) {
      occur++;
    }
  }
  return occur;
};
