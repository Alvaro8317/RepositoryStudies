const countNumbers = (n) => {
  for (let i = 0; i < n; i++) {
    console.log(i);
  }
};

const repeatArray = (array) => {
  let arrayRepeated = array;
  return arrayRepeated;
};

const convertToString = (array) => {
  let result = array.map((value) => value.toString());
  return result;
};

const twoDimensions = (value) => {
  let x = new Array(value);
  for (let i = 0; i < value; i++) {
    x[i] = new Array(value).fill(i);
  }
  return x;
};

// console.log(convertToString([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
console.log(twoDimensions(5));
