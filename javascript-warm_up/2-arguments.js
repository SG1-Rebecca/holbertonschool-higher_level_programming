#!/usr/bin/node

const NB_ARGS = process.argv.length;

if (NB_ARGS === 2) {
  console.log('No argument');
} else if (NB_ARGS === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
