#!/usr/bin/node

const request = require('request');
const urlpath = process.argv[2];
const users = {};

function sorter (todos) {
  todos.forEach((todo) => {
    if (!(todo.userId in users) && todo.completed) {
      users[todo.userId] = 0;
    }
    if (todo.completed) {
      users[todo.userId] += 1;
    }
  });
}

request.get(urlpath, 'utf-8', (err, res, bdy) => {
  if (err) {
    console.log(err);
  }

  if (res.statusCode === 200) {
    const data = JSON.parse(bdy);
    sorter(data);
    console.log(users);
  }
});
