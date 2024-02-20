#!/usr/bin/node

const request = require('request');
const id = 18;

const urlpath = process.argv[2];
const person = `https://swapi-api.alx-tools.com/api/people/18/`


function count(films) {
  let num = 0
  for (const film of films){
    if (film.characters.includes(person)){
      num += 1
    }
  }
  return num
}


request(urlpath, (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  bdy = JSON.parse(bdy);
  console.log(count(bdy.results))
});

