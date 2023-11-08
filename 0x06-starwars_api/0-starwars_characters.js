#!/usr/bin/node
// """Star Wars using Star wars API """;

const request = require('request');

const baseUrl = 'https://swapi.dev/api/';
const movieId = process.argv[2];

const getMovieData = () => {
  return new Promise((resolve, reject) => {
    const movieUrl = `${baseUrl}/films/${movieId}`;
    request(movieUrl, (error, response, movieData) => {
      try {
        if (!error && response.statusCode === 200) {
          const movie = JSON.parse(movieData);
          resolve(movie);
        } else {
          throw new Error('Error fetching movie data');
        }
      } catch (error) {
        reject(error.message);
      }
    });
  });
};

// fetch the character and print them.
const fetchAndPrintCharacters = (movie) => {
  return new Promise((resolve, reject) => {
    console.log(`Characters in ${movie.title} (Episode ${movie.episode_id}):`);
    const characterURLs = movie.characters;

    const characterPromises = characterURLs.map((characterURL) => {
      return new Promise((resolve, reject) => {
        request(characterURL, (error, response, characterData) => {
          try {
            if (!error && response.statusCode === 200) {
              const character = JSON.parse(characterData);
              console.log(character.name);
              resolve();
            } else {
              throw new Error('Error fetching character data');
            }
          } catch (error) {
            reject(error.message);
          }
        });
      });
    });
    Promise.all(characterPromises)
      .then(() => {
        resolve();
      })
      .catch((error) => {
        reject(error);
      });
  });
};

// check for movieId
const log = console.log;
if (!movieId) {
  log('Please provide movie ID as a command line argument.');
} else {
  getMovieData(movieId)
    .then((movie) => {
      return fetchAndPrintCharacters(movie);
    })
    .then(() => {
      log('All characters fetched and printed.');
    })
    .catch((error) => {
      log.error(error);
    });
}
