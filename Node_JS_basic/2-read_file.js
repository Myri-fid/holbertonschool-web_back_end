const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');

    const fields = {};
    let total = 0;

    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line === '') continue;

      const parts = line.split(',');
      const name = parts[0];
      const field = parts[parts.length - 1];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(name);
      total++;
    }

    console.log('Number of students: ' + total);

    for (let field in fields) {
      const list = fields[field];
      console.log('Number of students in ' + field + ': ' + list.length + '. List: ' + list.join(', '));
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
