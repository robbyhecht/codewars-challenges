// TECHNIQUES USED:
// split, for loop, conditionals

function iqTest(numbers) {
  //   make into an array
  numbers = numbers.split(" ")
  //  set counters to 0 for odds and evens in numbers array
  console.log(numbers)
  let countOdd = 0
  let countEven = 0
  let resultOdd = ""
  let resultEven = ""
//   loop through the array to set counters
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      countEven++
//    when there is an even number, the result is registered (with +1 per the instructions).
//    This index will matter if it is the only instance, aka the solution to this challenge.
      resultEven = i + 1
    }
    else if (numbers[i] % 2 === 1) {
      countOdd++
//    when there is an odd number, the result is registered
      resultOdd = i + 1
    }
//  return the result of the odd/even index for the instance that only occurs once
    if (countOdd === 1 && countEven > 1) {
      return resultOdd
    }
    else if (countEven === 1 && countOdd > 1) {
      return resultEven
    }
  }
}


// tests:

console.log(iqTest("2 4 7 8 10")) //3
console.log(iqTest("1 2 2")) //1
console.log(iqTest("2 63 81 1")) //1

// Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

// ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)