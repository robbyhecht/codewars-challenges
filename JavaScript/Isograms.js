// TECHNIQUES USED: 
// nested for loops, toLowerCase, split, conditionals

function isIsogram(str){
// need to compare each value with the following values in the array

  // case-sensitive
  str = str.toLowerCase()
  // create an array
  str = str.split("")
  // loop through letters
  for (let i=0; i<str.length; i++) {
    // loop through adjascent letters
    for (let j = i+1; j < str.length; j++) {
      // if letters match, it's not an isogram
      if (str[i] === str[j]) {
        return false
      }
    }
  }
  // if the internal return never happens...
  return true
}


// tests:
console.log( isIsogram("Dermatoglyphics")); //true
console.log( isIsogram("isogram")); //true
console.log( isIsogram("aba"), "same chars may not be adjacent" ); //false
console.log( isIsogram("moOse"), "same chars may not be same case" ); //false
console.log( isIsogram("isIsogram")); //false
console.log( isIsogram(""), "an empty string is a valid isogram" ); //true

// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.