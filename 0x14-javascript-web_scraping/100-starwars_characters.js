#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const charactersUrls = JSON.parse(body).characters;
  charactersUrls.forEach((character) => {
    request.get(character, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  });
});
