#!/usr/bin/node

const readfile = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
	if (err) {
		console.log(err);
	}
	else {
		console.log(data);
	}
});
