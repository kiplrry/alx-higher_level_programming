#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];
const filmurl = `https://swapi-api.alx-tools.com/api/films/${filmid}/`;
const peopleurl = 'https://swapi-api.alx-tools.com/api/people/';
const regex = /\d+/;

function charIds (characters) {
  const ids = [];
  characters.forEach(character => {
    const match = character.match(regex);
    if (match) {
      ids.push(match[0]);
    }
  });
  return ids;
}

// async function getNames (ids) {
//   const names = [];
//   console.log(`ids: ${ids}`);
//   ids.forEach(async id => {
//     const personurl = `${peopleurl}${id}/`;
//     request.get(personurl, 'utf-8', async (err, res, bdy) => {
//       if (err) {
//         console.log(err);
//       }
//       const name = await JSON.parse(bdy).name;
//       names.push(name);
//     });
//   });
//   return names;
// }

request.get(filmurl, 'utf-8', (err, res, bdy) => {
  if (err) {
    console.log(err);
  }
  const names = [];
  const filmjson = JSON.parse(bdy);
  const characters = filmjson.characters;
  const ids = charIds(characters);
  ids.forEach(id => {
    const personurl = `${peopleurl}${id}/`;
    request.get(personurl, 'utf-8', (err, res, bdy) => {
      if (err) {
        console.log(err);
      }
      const name = JSON.parse(bdy).name;
      names.push(name);
    });
  });
  setTimeout(() => {
    console.log(names);
  }, 5000);
  console.log(names);
});
