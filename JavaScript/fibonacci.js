// in an array:
// - a and b are the first two numbers 
// - n represents the nth term

let fib = (a, b, n) => {
  count = 0
  while (count < (n - 1)) {
    sum = a + b
    a = b
    b = sum
    count += 1
  }
  return a
}

console.log(fib(0, 1, 10)) //34
console.log(fib(3, 5, 3)) //8