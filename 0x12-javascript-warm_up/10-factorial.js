#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  }
  if (n === 0 || n === 1) {
    return 1; // Base case: Factorial of 0 and 1 is 1
  }
  return (n * factorial(n - 1)); // Recursive case
}

const arg = parseInt(process.argv[2], 10);

if (!isNaN(arg)) {
  const result = factorial(arg);
  console.log(result);
} else {
  console.log(1);
}
