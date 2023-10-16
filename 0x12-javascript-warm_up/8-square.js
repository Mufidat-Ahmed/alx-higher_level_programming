#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg, 10);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let x = '';
    for (let j = 0; j < size; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
