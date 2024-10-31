const countNumbers = (n) => {
  for (let i = 0; i < n; i++) {
    console.log(i);
  }
};

console.time('The algorithm had');
countNumbers(5);
console.timeEnd('The algorithm had');
