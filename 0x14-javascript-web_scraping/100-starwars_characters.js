#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];
const filmurl = `https://swapi-api.alx-tools.com/api/films/${filmid}/`;

function getNames (charUrls) {
  charUrls.forEach(charUrl => {
    request(charUrl, 'utf-8', (err, res, bdy) => {
      if (err) {
        console.log(err);
      }
      const name = JSON.parse(bdy).name;
      console.log(name);
    });
  });
}

request.get(filmurl, 'utf-8', (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  const filmjson = JSON.parse(bdy);
  const characters = filmjson.characters;
  getNames(characters);
});
