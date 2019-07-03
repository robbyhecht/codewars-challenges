// TECHNIQUES USED:
// for loop

function sum (numbers) {
  sum_all = 0
  for (let i = 0; i < numbers.length; i++) {
    sum_all += numbers[i]
  }
  return sum_all
};


console.log(sum([])) //0
console.log(sum([1, 5.2, 4, 0, -1])) //9.2

// Write a method sum (sum_array in python, SumArray in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.