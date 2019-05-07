#!/usr/bin/node
// JS Script

let num = parseInt(process.argv[2]);

if (num) {
  for (let i = 0; i < num; i++) {
    console.log('x'.repeat(num));
  }
} else {
  console.log('Missing size');
}
