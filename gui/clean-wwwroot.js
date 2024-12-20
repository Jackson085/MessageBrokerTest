// clean-wwwroot.js

const fs = require('fs');
const path = require('path');

const wwwrootPath = path.join(__dirname, '..', 'wwwroot');

// Überprüfe, ob der wwwroot-Ordner existiert
if (fs.existsSync(wwwrootPath)) {
  // Lösche den wwwroot-Ordner und alle seine Unterordner und Dateien rekursiv
  fs.rmSync(wwwrootPath, { recursive: true });
  console.log('wwwroot-Ordner erfolgreich gelöscht.');
} else {
  console.log('wwwroot-Ordner existiert nicht.');
}
