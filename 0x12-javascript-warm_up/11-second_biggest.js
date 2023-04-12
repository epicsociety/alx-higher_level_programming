#!/usr/bin/node

// convert arguments to an array of numbers
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  // initialize secondMax to a very small value
  let secondMax = -Infinity;
  for (let i = 0; i < args.length; i++) {
    if (args[i] !== max && args[i] > secondMax) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
