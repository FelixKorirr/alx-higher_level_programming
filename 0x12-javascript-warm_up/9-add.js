#!/usr/bin/node
function add (x, y)
{
    const z = x + y;
    console.log(z);
}

add(Number(process.argv[2]), Number(process.argv[3]));