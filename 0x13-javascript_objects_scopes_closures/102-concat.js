#!/usr/bin/node
const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log('Concatenation complete. Result saved to ' + destinationFile);
      }
    });
  });
});
