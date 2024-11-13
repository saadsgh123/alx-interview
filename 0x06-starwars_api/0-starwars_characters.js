#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${filmId}/`,
  method: 'GET'
};

request(options, (error, response, body) => {
  if (error) {
    console.error('Error making API request:', error);
    return;
  }

  const data = JSON.parse(body);

  if (data && data.characters) {
    printCharacters(data.characters, 0);
  } else {
    console.log(`Request failed with status code: ${response.statusCode}`);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
