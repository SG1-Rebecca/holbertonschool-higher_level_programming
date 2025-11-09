#!/usr/bin/node

const VALUE_ARGS = process.argv[2];

if (VALUE_ARGS === undefined) {
  console.log('No argument');
} else {
  console.log(VALUE_ARGS);
}
