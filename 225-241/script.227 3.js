function func1() {
    return 3;
}
// Присваиваем func2 ссылку на функцию func1
let func2 = func1;
// Выводим сумму результатов работы обеих функций
console.log(func1() + func2());