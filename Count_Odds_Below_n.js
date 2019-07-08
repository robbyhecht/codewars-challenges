// TECHNIQUES USED:
// Math.floor

function oddCount(n){
  return Math.floor(n/2)
}

// Given a number n, return the number of positive odd numbers below n, EASY!
console.log(oddCount(7)) //=> 3, i.e [1, 3, 5]
console.log(oddCount(15)) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

// [8]