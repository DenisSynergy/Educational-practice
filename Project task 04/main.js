        // Проверка значений из инпутов
        function getNumbers() {
            const num1 = document.getElementById('number1').value;
            const num2 = document.getElementById('number2').value;
            const resultWindow = document.getElementById('result');

            // Проверка на пустые значения
            if (num1 === '' || num2 === '') {
                resultWindow.textContent = 'Error: Введите число';
                resultWindow.className = 'resultWindow error';
                return null;
            }

            // Преобразование в числа
            const number1 = parseFloat(num1);
            const number2 = parseFloat(num2);

            // Проверка на валидность чисел
            if (isNaN(number1) || isNaN(number2)) {
                resultWindow.textContent = 'Error: Введите число';
                resultWindow.className = 'resultWindow error';
                return null;
            }

            return { number1, number2 };
        }

        // Функция для отображения результата
        function displayResult(value, isError = false) {
            const resultWindow = document.getElementById('result');
            resultWindow.textContent = value;
            resultWindow.className = isError ? 'resultWindow error' : 'resultWindow success';
        }

        // Сумма
        function calculateSum() {
            const numbers = getNumbers();
            if (numbers === null) return;
            
            const result = numbers.number1 + numbers.number2;
            displayResult(`= ${result}`);
        }

        // Разность
        function calculateSubtract() {
            const numbers = getNumbers();
            if (numbers === null) return;
            
            const result = numbers.number1 - numbers.number2;
            displayResult(`= ${result}`);
        }

        // Умножение
        function calculateMultiply() {
            const numbers = getNumbers();
            if (numbers === null) return;
            
            const result = numbers.number1 * numbers.number2;
            displayResult(`= ${result}`);
        }

        // Деление
        function calculateDivide() {
            const numbers = getNumbers();
            if (numbers === null) return;
            
            if (numbers.number2 === 0) {
                displayResult('Error: Делить на ноль нельзя!', true);
                return;
            }
            
            const result = numbers.number1 / numbers.number2;
            displayResult(`= ${result}`);
        }