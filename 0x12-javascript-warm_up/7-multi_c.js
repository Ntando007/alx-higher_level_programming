#!/usr/bin/node
const str = ('C is fun');
let x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log("Missing number of occurrences")
} else {
  for (let i = 0; i < x; i++) {
      console.log(str);
  }
}
