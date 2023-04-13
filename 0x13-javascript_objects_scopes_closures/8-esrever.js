#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  for (let i = 0; i < len; i++, len--) {
    const temp = list[i];
    list[i] = list[len];
    list[len] = temp;
  }
  return list;
};
