#!/usr/bin/node
const num = parseInt(+process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let ind = num; ind > 0; ind--) {
    console.log('C is fun');
  }
}
