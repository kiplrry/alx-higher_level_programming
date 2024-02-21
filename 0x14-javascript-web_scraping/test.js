#!/usr/bin/node

async function pushNumbers () {
  const numbers = [];

  // Asynchronous loop using setTimeout
  for (let i = 0; i < 5; i++) {
    await new Promise(resolve => {
      setTimeout(() => {
        numbers.push(i + 1); // Pushing numbers to the array
        resolve(); // Resolving the promise after 1 second
      }, 1000);
    });
  }

  return numbers; // Returning the array after the loop completes
}

// Example usage
pushNumbers()
  .then(numbers => {
    console.log('Numbers:', numbers); // Output the array of numbers
  })
  .catch(error => {
    console.error('Error:', error);
  });
