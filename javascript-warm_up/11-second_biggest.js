#!/usr/bin/node

const ARGS = process.argv.slice(2);

if (ARGS.length <= 1) {
  console.log(0);
} else {
  const numbers = ARGS.map(Number);
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
