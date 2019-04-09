// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
// Note: If the number is a multiple of both 3 and 5, only count it once.


function solution(number) {
  //   create empty array to fill with qualified numbers
    let newArray = [0]
  //   loop through all values between 1 and number, grabbing only those that fit the instructions
    for (let i = 1; i < number; i++) {
      if (i % 3 === 0 && i % 5 === 0
      || i % 3 === 0
      || i % 5 === 0) {
  //   add each qualified number to newArray
        newArray.push(i)
      }
    }
  //   make a quick anonymous function to reduce array to its sum
    let sum = newArray.reduce((num, a) => (num + a))
    return(sum)
  }

  console.log(solution(10)) //23
  console.log(solution(23)) //119
  console.log(solution(2)) //0