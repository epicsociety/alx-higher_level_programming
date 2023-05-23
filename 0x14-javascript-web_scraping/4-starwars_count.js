#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
  console.log(count.length);
});
