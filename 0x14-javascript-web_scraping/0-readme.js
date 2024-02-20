#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];

fs.readFile(fp, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
