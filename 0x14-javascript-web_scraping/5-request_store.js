#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const urlpath = process.argv[2];
const fp = process.argv[3];

request.get(urlpath, 'utf-8', (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const data = bdy;
    fs.writeFile(fp, data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
