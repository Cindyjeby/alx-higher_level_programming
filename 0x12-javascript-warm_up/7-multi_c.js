#!/usr/bin/node

const x = process.argv[2];
if (isNaN(x)) {
	console.log('Missing number of occurances');
} else {
	for (let counter = 0; counter < x; counter++) {
		cosole.log('C is fun');
	}
}
