#!/usr/bin/node
exports.callMeMoby = function (i, theFunction) {
  for (let j = 0; j < i; j++) {
    theFunction();
  }
};
