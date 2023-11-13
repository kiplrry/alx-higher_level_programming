#!/usr/bin/node
const num = parseInt(+process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = num; i > 0; i--) {
    for (let j = num; j > 0; j--) {
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
