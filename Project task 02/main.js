/*
 * JavaScript для кейс-задачи № 2
 
 * - Увеличение/уменьшение значения при нажатии на кнопки "+" и "-"
 * - Изменение цвета фона табло в зависимости от значения
 * - Деактивация кнопок при значениях 10 и -10
 * - Вывод сообщения об экстремальном значении
 */

// Получение ссылок на элементы DOM
// Элемент для отображения результата счетчика
const resultElement = document.getElementById('result');
// Кнопка "плюс" для увеличения значения
const plusBt = document.getElementById('Btplus');
// Кнопка "минус" для уменьшения значения
const minusBt = document.getElementById('Btminus');
// Элемент для отображения сообщения об экстремальном значении
const extrMess = document.getElementById('extrMess');

// Первоначальное значение счетчика 0
let counter = 0;

//Смена цвета табло счетчика (увеличение-желтый, 0-красный, уменьшение-зеленый)
function boardColor() {
    // Если значение > 0
    if (counter > 0) {
        // Желтый цвет табло при увиличении значений
        resultElement.style.backgroundColor = 'yellow';
        resultElement.style.color = '#000000ff';
    }
    // Если значение < 0
    else if (counter < 0) {
        // Зеленый цвет табло при уменьшении значений
        resultElement.style.backgroundColor = 'green';
        resultElement.style.color = 'white';
    }
    // Если значение равно нулю
    else {
        // Красный цвет табло при 0
        resultElement.style.backgroundColor = 'red';
        resultElement.style.color = 'white';
    }
}

// Деактивация кнопок "+" и "-" Btdisable
function Btdisable() {
    // Если значение 10, деактивируем кнопку "плюс"
    if (counter === 10) {
        // Установка атрибута disabled
        plusBt.disabled = true;
    }
    // Если значение -10, деактивируем кнопку "минус"
    else if (counter === -10) {
        // Установка атрибута disabled
        minusBt.disabled = true;
    }
    //  Активируем обе кнопки для всех остальных значений
    else {
        // Для активации кнопки "плюс"
        plusBt.disabled = false;
        // Для активации кнопки "минус"
        minusBt.disabled = false;
    }
}

/* Функция для вывода сообщения об экстремальном значении при достижении 10 или -10 */

function updateExtrMess() {
    // Если значение равно 10 или -10
    if (counter === 10 || counter === -10) {
        // Установка текста сообщения
        extrMess.innerText = 'Вы достигли\n экстремального значения!';
        // Добавление класса "show" для отображения сообщения
        extrMess.classList.add('show');
    }
    // Скрываем сообщение для всех остальных значений
    else {
        // Удаление класса "show" для скрытия сообщения
        extrMess.classList.remove('show');
        // Очистка текста сообщения
        extrMess.textContent = '   ';
    }
}

/* Функция для вывода значения счетчика после каждого изменения значения */

function Display() {
    // Обновление текстового содержимого табло результата
    resultElement.textContent = counter;
    // Обновление цвета фона табло в зависимости от значения
    boardColor();
    // Обновление состояния кнопок (активация/деактивация)
    Btdisable();
    // Обновление сообщения об экстремальном значении
    updateExtrMess();
}

/* Обработчик события увеличивает значение счетчика на единицу после клика на кнопку "плюс" */
function handlePlusClick() {
    // Увеличение значения на 1
    counter++;
    // Обновление отображения всех элементов
    Display();
}

/* Обработчик события уменьшает значение счетчика на единицу после клика на кнопку "минус" */
function handleMinusClick() {
    // Уменьшение значения на 1
    counter--;
    // Обновление отображения всех элементов интерфейса
    Display();
}

// Слушатель события "click" на кнопку "плюс"
// При клике вызывается функция handlePlusClick
plusBt.addEventListener('click', handlePlusClick);

// Слушатель события "click" на кнопку "минус"
// При клике вызывается функция handleMinusClick
minusBt.addEventListener('click', handleMinusClick);

// Обновление отображения всех элементов интерфейса
Display();