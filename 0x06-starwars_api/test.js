#!/usr/bin/node

const request = require('request');

// Check if the Movie ID argument is provided
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL to the Star Wars API for the specified movie
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  // Parse the response body to JSON
  const filmData = JSON.parse(body);

  // Get the list of character URLs from the film data
  const characterUrls = filmData.characters;

  // Iterate through each character URL and make a request to get the character name
  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
      }

      // Parse the character data
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
