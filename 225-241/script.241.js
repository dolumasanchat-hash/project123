const calculator = {
  // 1. Сумма элементов массива
  sum: function(arr) {
    return arr.reduce((acc, num) => acc + num, 0);
  },

  // 2. Сумма квадратов элементов массива
  sumOfSquares: function(arr) {
    return arr.reduce((acc, num) => acc + num ** 2, 0);
  },

  // 3. Сумма кубов элементов массива
  sumOfCubes: function(arr) {
    return arr.reduce((acc, num) => acc + num ** 3, 0);
  }
};

const numbers = [1, 2, 3];

console.log(calculator.sum(numbers));        // 6   (1 + 2 + 3)
console.log(calculator.sumOfSquares(numbers)); // 14 (1^2 + 2^2 + 3^2)
console.log(calculator.sumOfCubes(numbers));   // 36 (1^3 + 2^3 + 3^3)