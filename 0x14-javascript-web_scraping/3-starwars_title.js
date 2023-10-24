#!/usr/bin/node

//import request module
const request = require('request');

// the first argument is the movie Id
const movieId = process.argv[2];

//construct the API URL with the provided movie id
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

//make HTTP GET request to the api
request(apiUrl, function (err, response, body) {
	if (err) {
		console.log(err);
	} else {
		const content = JSON.parse(body);
		console.log(content.title);
	}
});
