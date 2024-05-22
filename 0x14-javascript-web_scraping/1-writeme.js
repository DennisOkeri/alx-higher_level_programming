#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

if (!filePath || !stringToWrite) {
  console.error('Usage: ./write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
