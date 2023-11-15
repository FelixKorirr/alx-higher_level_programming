#!/usr/bin/node
const dict = require("./101-data").dict;

const totalist = Object.entries(dict);
const v = Object.values(dict);
const valUniq = [...new Set(v)];
const newDict = {};
for (const y in valUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valUniq[y]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valUniq[y]] = list;
}
console.log(newDict);
