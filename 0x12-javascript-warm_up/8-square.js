#!/usr/bin/node

const firstArgument = parseInt(process.argv[2]);

if (isNaN(firstArgument)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgument; i++) {
    let row = [];
    for (let j = 0; j < firstArgument; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
