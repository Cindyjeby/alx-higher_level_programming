#!/usr/bin/node

//import request module
const request = require('request');

//first argument is the URL to request GET
const url = process.argv[2];

//make an HTTP GET request
request(url, function (err, response, body) {
	if (err) {
		console.error(err);
	} else {
		console.log('code:', response.statusCode);
	}
});
