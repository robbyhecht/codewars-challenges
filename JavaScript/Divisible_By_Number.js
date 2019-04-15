// Complete the function which takes two arguments and returns all numbers which are divisible by given divisor. First argument is an array of numbers and the second is the divisor.


let divisibleBy = (numbers, divisor) => {
  let newArray = []  //begin with an empty array to return
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % divisor === 0) {
      newArray.push(numbers[i])  //push numbers into newArray if divisible by divisor
    }
  }
  return newArray
}


console.log(divisibleBy([2, 34, 8, 3, 16], 4)) //[8, 16]