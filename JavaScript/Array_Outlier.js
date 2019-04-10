// You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

function findOutlier(integers) {
  let numsBool
  // Compare the first three integers two at a time to find a matching pair of even or odd.
  for (i=0; i<integers.length; i++) {
    if (integers[i] >= 0) {
      if (integers[0] % 2 === 0 && integers[1] % 2 === 0) {
        numsBool = 0
      }
      else if (integers[0] % 2 !== 0 && integers[1] % 2 !== 0) {
        numsBool = 1
      }
      else if (integers[1] % 2 === 0 && integers[2] % 2 === 0) {
        numsBool = 0
      }  
      else if (integers[1] % 2 !== 0 && integers[2] % 2 !== 0) {
        numsBool = 1
      } 
      else if (integers[0] % 2 === 0 && integers[2] % 2 === 0) {
        numsBool = 0
      }  
      else if (integers[0] % 2 !== 0 && integers[2] % 2 !== 0) {
        numsBool = 1
      } 
    }
  }
  // The outlier in the array is whichever integer does not match the matching pair from above
  for (i=0; i<integers.length; i++) {
    if (integers[i] % 2 !== numsBool) {
      let N = integers[i]
      return N
    }
  }
}

// tests:

console.log(findOutlier([0, 1, 2])) //1
console.log(findOutlier([1, 2, 3])) //2
console.log(findOutlier([2,6,8,10,3])) //3
console.log(findOutlier([0,0,3,0,0])) //3
console.log(findOutlier([1,1,0,1,1])) //0
console.log(findOutlier([-2,1,1,1])) //-2