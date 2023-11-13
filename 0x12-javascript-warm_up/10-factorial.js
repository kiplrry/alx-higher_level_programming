#!/usr/bin/node
const factnum = parseInt(+process.argv[2]);

function factorial (num) {
  if (num < 0) {
    return;
  }
  if (num === 1 || num === 0 || isNaN(num)) {
    return 1;
  }
  return num * factorial(--num);
}
const fact = factorial(factnum);
if (fact) {
  console.log(fact);
}
