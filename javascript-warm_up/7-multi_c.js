#!/usr/bin/node

const x = process.argv;
const num = Number.parseInt(x);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
}
