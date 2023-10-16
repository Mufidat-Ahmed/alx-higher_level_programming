#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const argA = parseInt(process.argv[2], 10);
const argB = parseInt(process.argv[3], 10);
if (!isNaN(argA) && !isNaN(argB)) {
  const result = add(argA, argB);
  console.log(result);
} else {
  console.log('NaN');
}
