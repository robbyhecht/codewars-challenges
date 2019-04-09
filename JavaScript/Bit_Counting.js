// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

var countBits = function(n) {
  // convert to binary and make var
    let binaryN = n.toString(2)
  // split, loop, add and make sum var
    let binarySum = binaryN
      .split('')
      .map(Number)
      .reduce(function (a, b) {
          return a + b;
      }, 0);
  // return sum of number which is the same as the sum of the 1 digits  
    return binarySum
  }

  
// tests:

console.log(countBits(0)); //0
console.log(countBits(4)); //1
console.log(countBits(7)); //3
console.log(countBits(9)); //2
console.log(countBits(10)); //2