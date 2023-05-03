#!/usr/bin/node

const readfile = require('readfile');

readfile.readFile(process.arg[2], 'utf-8, (err, data) => {
if (err) {
	console.log(err);
}
else {
console.log(data);
}
});
