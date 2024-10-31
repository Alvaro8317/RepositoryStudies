const countNumbers = (n) => {
  for (let i = 0; i < n; i++) {}
};

let start = performance.now();
countNumbers(5);
let end = performance.now();
const duration = end - start;
console.log('The algorithm had', duration, 'ms');
