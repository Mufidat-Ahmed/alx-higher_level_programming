#!/usr/bin/node
const { dict } = require('./101-data');

const userOcc = {};
for (const userid in dict) {
  const occ = dict[userid];
  if (userOcc[occ]) {
    userOcc[occ].push(userid);
  } else {
    userOcc[occ] = [userid];
  }
}
console.log(userOcc);
