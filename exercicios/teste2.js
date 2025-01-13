// 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

// IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

function verificaFibonacci(numero) {
  // Inicializa os dois primeiros valores da sequência
  let a = 0;
  let b = 1;

  // Verifica se o número é 0 ou 1, que pertencem à sequência
  if (numero === 0 || numero === 1) {
    return `O número ${numero} pertence à sequência de Fibonacci.`;
  }

  // Calcula a sequência até que o número seja alcançado ou ultrapassado
  while (b < numero) {
    let temp = b;
    b = a + b; // Soma dos dois últimos valores
    a = temp;
  }

  // Verifica se o número informado é igual ao último valor calculado
  if (b === numero) {
    return `O número ${numero} pertence à sequência de Fibonacci.`;
  } else {
    return `O número ${numero} NÃO pertence à sequência de Fibonacci.`;
  }
}

// Número informado (pode ser substituído por uma entrada do usuário)
const numero = 21; // Exemplo de entrada

console.log(verificaFibonacci(numero));
// Saída: O número 21 pertence à sequência de Fibonacci.