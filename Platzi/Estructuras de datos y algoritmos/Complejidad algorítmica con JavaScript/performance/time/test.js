const countNumbers = (n) => {
  for (let i = 0; i < n; i++) {}
};

let totalDuration = 0;
const iterations = 10000; // Número de iteraciones

for (let j = 0; j < iterations; j++) {
  let start = performance.now();
  countNumbers(5);
  let end = performance.now();
  totalDuration += end - start;
}

console.log('Average time per execution:', totalDuration / iterations, 'ms');
