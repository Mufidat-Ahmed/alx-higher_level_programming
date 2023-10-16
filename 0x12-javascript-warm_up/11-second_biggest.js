#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
} else {
  const nums = args.map(arg => parseInt(arg, 10)).filter(Number.isInteger);
  if (nums.length < 2) {
    console.log('0');
  } else {
    const sortednum = nums.sort((a, b) => b - a);
    console.log(sortednum[1]);
  }
}
