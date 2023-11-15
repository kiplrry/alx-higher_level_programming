#!/usr/bin/node
const listObj = require('./100-data');
const list = listObj.list;
console.log(list);
const newlist = list.map((item, index) => item * index);
console.log(newlist);
