#!/usr/bin/node

//import module
const fs = require('fs');

//first argument is the file path
const filePath = process.argv[2];

//second argument is the string to write
const content = process.argv[3];

//write content into file in utf-8
fs.writeFile(filePath,content, 'utf-8', (err) => {
	if (err) {
		console.log(err);
	}
});
