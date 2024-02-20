#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

const urlpath = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(urlpath, (err, res, bdy) => {
  // console.log(`code: ${res.statusCode}`);
  if (err) {
    console.log(err);
  }
  bdy = JSON.parse(bdy);
  console.log(bdy.title);
});
