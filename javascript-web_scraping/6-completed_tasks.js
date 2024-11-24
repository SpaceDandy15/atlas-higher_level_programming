#!/usr/bin/node

// Import the request module
const request = require('request');

// Fetch data from the given API URL
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log('Error fetching data:', error);
    return;
  }

  // Parse the response body (which is in JSON format)
  const tasks = JSON.parse(body);
  
  // Create an object to store the count of completed tasks for each user
  const userTasksCount = {};

  // Iterate through the tasks and count the completed ones for each user
  tasks.forEach(task => {
    if (task.completed) {
      // If the user already has a count, increment it; otherwise, set it to 1
      if (userTasksCount[task.userId]) {
        userTasksCount[task.userId]++;
      } else {
        userTasksCount[task.userId] = 1;
      }
    }
  });

  // Print the results (only users with completed tasks)
  console.log(userTasksCount);
});
