#!/usr/bin/node

const https = require("https");

https
    .get(`https://swapi-api.alx-tools.com/api/`, resp => {
      let data = "";

      // A chunk of data has been recieved.
      resp.on("data", chunk => {
        data += chunk;
      });

      // The whole response has been received. Print out the result.
      resp.on("end", () => {
        let url = JSON.parse(data).message;
        console.log(url);
      });
    })
    .on("error", err => {
      console.log("Error: " + err.message);
    });
