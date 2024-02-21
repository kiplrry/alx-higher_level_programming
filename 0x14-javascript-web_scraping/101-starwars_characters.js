#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];
const filmurl = `https://swapi-api.alx-tools.com/api/films/${filmid}/`;

async function getNames (charUrls) {
  const names = [];
  for (const charUrl of charUrls) {
    await new Promise((resolve) => {
      request.get(charUrl, 'utf-8', (err, res, body) => {
        if (err) {
          console.log(err);
        }
        const name = JSON.parse(body).name;
        names.push(name);
        resolve();
      });
    });
  }
  return names;
}

request.get(filmurl, 'utf-8', (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  const filmjson = JSON.parse(bdy);
  const charUrls = filmjson.characters;
  getNames(charUrls).then((res) => {
    res.forEach(result => {
      console.log(result);
    });
  });
});
