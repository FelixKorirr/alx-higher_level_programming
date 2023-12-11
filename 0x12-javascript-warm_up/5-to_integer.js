#!/usr/bin/node

const len = process.argv.length;
const firstValue = parseInt(process.argv[2]);

if ((len <= 2) || (isNaN(firstValue))) {
  console.log('Not a number');
} else if (len > 2) {
  console.log(`My number: ${firstValue}`);
}
