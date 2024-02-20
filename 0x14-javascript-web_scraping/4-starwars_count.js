#!/usr/bin/node

const request = require('request');
const id = 18;

const urlpath = `https://swapi-api.alx-tools.com/api/people/${id}/`;

request(urlpath, (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  bdy = JSON.parse(bdy);
  console.log(bdy.films.length);
});
