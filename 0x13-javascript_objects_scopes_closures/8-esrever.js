#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let x = 0;
  while (len - x > 0) {
    const a = list[len];
    list[len] = list[x];
    list[x] = a;
    x++;
    len--;
  }
  return list;
};
