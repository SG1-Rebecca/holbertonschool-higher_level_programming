#!/usr/bin/node

const x = parseInt(process.argv[2]);
const numb = Number.parseInt(x);

if (isNaN(numb)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < numb; index++) {
    console.log('C is fun');
  }
}
