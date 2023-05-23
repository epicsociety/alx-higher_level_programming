#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
