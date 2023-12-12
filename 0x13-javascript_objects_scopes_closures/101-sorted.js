#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const x in totalist) {
    if (totalist[x][1] === valsUniq[j]) {
      list.unshift(totalist[x][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
