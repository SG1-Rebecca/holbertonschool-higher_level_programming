#!/usr/bin/node

const VALUE_ARGS = process.argv[2];

if (VALUE_ARGS === undefined) {
  console.log('No argument passed');
} else {
  console.log(VALUE_ARGS);
}
