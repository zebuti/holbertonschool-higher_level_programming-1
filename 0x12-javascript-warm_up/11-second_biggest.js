#!/usr/bin/node
// JS Script

let argsLen = process.argv.length;
if (argsLen === 2 || argsLen === 3) {
  console.log('0');
} else {
  let arr = [];
  for (let i = 2; i < argsLen; i++) {
    arr.push(process.argv[i]);
  }
  console.log(arr.sort()[arr.length - 2]);
}
