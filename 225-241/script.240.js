const obj = {
  first:  function() { return 1; },
  second: function() { return 2; },
  third:  function() { return 3; }
};

// Находим сумму и выводим в консоль
const sum = obj.first() + obj.second() + obj.third();
console.log(sum); // 6