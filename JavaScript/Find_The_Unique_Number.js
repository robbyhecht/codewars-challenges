// TECHNIQUES USED:
// for loop, conditionals, sort

function findUniq(arr) {
    arr = arr.sort() // unique number will shift to the beginning or end of the array
    if (arr[0] !== arr[1]) {
        return arr[0]
    }
    else {
        return arr[arr.length - 1]
    }
}

// OR MORE PRIMITIVE--

function findUniq(arr) {

    //   check first two numbers
    if (arr[0] !== arr[1] && arr[1] === arr[2]) {
        return arr[0]
    }
    else if (arr[0] !== arr[1] && arr[1] !== arr[2]) {
        return arr[1]
    }
    //   if not those, loop through the array
    else {
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] !== arr[i-1]) {
                return arr[i]
            }
        }
    }
}


// There is an array with some numbers. All numbers are equal except for one. Try to find it!
// findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
// findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
// It’s guaranteed that array contains more than 3 numbers.
// The tests contain some very huge arrays, so think about performance.

// [6]