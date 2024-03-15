const readline = require('readline');

const wAlg = (n) => {
  let sequencia = [n];
  while (n != 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = (n * 3) + 1;
    }
    sequencia.push(n);
  }
  return sequencia.join(' ');
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (input) => {
  const n = parseInt(input);
  console.log(wAlg(n));
  rl.close();
});
