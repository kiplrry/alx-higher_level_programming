#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let searchList = list;
  searchList = searchList.filter((val) => {
    return val === searchElement;
  });
  return searchList.length;
};
