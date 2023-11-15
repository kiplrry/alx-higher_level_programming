#!/usr/bin/node
const dict = require('./101-data').dict;
console.log(dict);

const newDict = {};
for (const key in dict) {
  const newDictVals = newDict[dict[key]];
  const prevVals = newDictVals || [];
  newDict[dict[key]] = [...prevVals, key];
}
console.log(newDict);
