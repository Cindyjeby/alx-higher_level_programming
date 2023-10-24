#!/usr/bin/node

// import fs module
const fs = require('fs');

//the first argument is the file path
const filePath = process.argv[2];

//content read in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error('Error reading file:', err);
		return;
	}
	console.log(data);
});
