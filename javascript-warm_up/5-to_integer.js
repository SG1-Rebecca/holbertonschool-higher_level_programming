#!/usr/bin/node

const nb = Number.parseInt(process.argv[2]);

if (isNaN(nb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nb);
}
