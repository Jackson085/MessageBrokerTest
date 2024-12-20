const fs = require('fs');
const { execSync } = require('child_process');

// Lese die angular.json-Datei ein
const angularJson = JSON.parse(fs.readFileSync('angular.json', 'utf-8'));

// Extrahiere die Namen der Projekte
const projectNames = Object.keys(angularJson.projects);

// Baue jedes Projekt
projectNames.forEach(projectName => {
  console.log(`Building project: ${projectName}`);
  try {
    execSync(`ng build --project=${projectName}`, { stdio: 'inherit' });
    console.log(`Project "${projectName}" built successfully.`);
  } catch (error) {
    console.error(`Error building project "${projectName}": ${error.message}`);
  }
});
