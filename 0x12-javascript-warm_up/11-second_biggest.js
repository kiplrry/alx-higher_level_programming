#!/usr/bin/node
const arr = process.argv.slice(2);
// h.sort()
const newArr = [];
arr.forEach((item, index) => {
  newArr[index] = parseInt(+item);
});
const compareFn = function (a, b) {
  if (a > b) {
    return 1;
  } else if (a < b) {
    return -1;
  }
  return 0;
};
const sortedArr = newArr.sort(compareFn);

console.log(sortedArr[sortedArr.length - 2]);
