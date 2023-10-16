#!/usr/bin/node
const arg = process.argv[2];
const intArg = parseInt(arg, 10);
if (!isNaN(intArg)) {
  console.log(`My number: ${intArg}`);
} else {
  console.log('Not a number');
}
