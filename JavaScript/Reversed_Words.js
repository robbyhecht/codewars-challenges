// TECHNIQUES USED:
// split, reverse, trim, join, descending for loop

function reverseWords(str) {
    let newStr = ""
    str = str.split(" ")
    for(let i = str.length - 1; i >= 0; i--) {
        newStr += str[i] + " "
    }
    str = newStr.trim()
    return str;
}

// OR

function reverseWords(str) {
    str = str.split(" ")
    .reverse()
    .join(" ")
    return str;
}