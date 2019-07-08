// TECHNIQUES USED:
// push, indexOf, for loop, conditionals, 

function gooseFilter (birds) {
  var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
  var filtered_birds = [] //set empty array
  for (let i = 0; i < birds.length; i++) {
    let bird = birds[i] 
    if (geese.indexOf(bird) === -1) { //using indexOf method
      filtered_birds.push(bird) //add to array
    }
  }
  console.log(filtered_birds)
  return filtered_birds
};

// OR

function gooseFilter (birds) {
  var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
  var filtered_birds = []
  for (let i = 0; i < birds.length; i++) {
    let bird = birds[i]
    if (geese.includes(bird) === false) { //using includes method, making sure to check for birds that are not included
      filtered_birds.push(bird)
    }
  }
  console.log(filtered_birds)
  return filtered_birds
};

// Write a function, gooseFilter/goose_filter/GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
// The geese are any strings in the following array, which is pre-populated in your solution:
// geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]