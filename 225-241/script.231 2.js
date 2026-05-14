// Попытка вызвать функцию до её объявления
try {
    console.log(sayHello());
} catch (error) {
    console.log('Ошибка:', error.message);
}

// Объявление функции как Function Expression
let sayHello = function() {
    return "Привет!";
};

// Вызов функции после объявления
console.log(sayHello()); // Выведет: Привет!