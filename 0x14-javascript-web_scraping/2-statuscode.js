#!/usr/bin/node

const request = require('request');

const urlpath = process.argv[2];

request(urlpath, (err, res) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${res.statusCode}`);
});
