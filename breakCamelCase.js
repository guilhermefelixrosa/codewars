/*
Kata training - Code Wars

Complete the solution so that the function will break up camel casing, using a space between words.

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

*/

// let example = solution("camelCasing");
let example = solution("camelCasingTest");
console.log(example);

function solution(string) {
  if (string == "") {
    return "";
  } else {
    let i,
      array = [],
      lastUpper;

    for (i = 0; i < string.length; i++) {
      if (isUpperCase(string[i])) {
        if (array.length == 0) {
          array.push(string.substring(0, i));
          array.push(string.substring(i));
          lastUpper = i;
        } else {
          array[array.length - 1] = string.substring(lastUpper, i);
          array.push(string.substring(i));
        }
      }
    }

    string = "";
    for (i = 0; i < array.length; i++) {
      string = string + " " + array[i];
    }
    string = string.trim();
    return string;
  }
}

function isUpperCase(char) {
  return char === char.toUpperCase();
}
