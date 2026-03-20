#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(size);
  for (let index = 0; index < size; index++) {
    console.log(row);
  }
}
