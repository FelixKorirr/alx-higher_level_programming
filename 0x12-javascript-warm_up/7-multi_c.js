#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
const myString = 'C is fun';

if (isNaN(arg1) || arg1 === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log(myString);
  }
}
