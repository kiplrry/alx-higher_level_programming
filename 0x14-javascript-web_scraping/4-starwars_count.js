#!/usr/bin/node

const request = require('request');
const id = 18;

const urlpath = process.argv[2];

function count (films) {
  let num = 0;
  for (const film of films) {
    film.characters.forEach((char) => {
      if (char.includes(id)) {
        num += 1;
      }
    });
  }
  return num;
}

request(urlpath, (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  bdy = JSON.parse(bdy);
  console.log(count(bdy.results));
});
