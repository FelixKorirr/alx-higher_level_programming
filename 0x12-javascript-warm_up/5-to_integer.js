#!/usr/bin/node
parsedValue = parseInt(process.argv[2])
if (isNaN(parsedValue) || parsedValue === undefined) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedValue}`);
}
