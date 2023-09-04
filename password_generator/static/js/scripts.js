// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    // Находим все кнопки "Скопировать"
    var copyButtons = document.querySelectorAll(".copy-button");

    // Добавляем обработчик события на каждую кнопку
    copyButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Получаем пароль из атрибута data-password
            var passwordToCopy = this.getAttribute("data-password");

            // Создаем временный элемент textarea для копирования
            var textArea = document.createElement("textarea");
            textArea.value = passwordToCopy;
            document.body.appendChild(textArea);

            // Выделяем текст в textarea
            textArea.select();
            textArea.setSelectionRange(0, 99999); // Для мобильных устройств

            // Копируем текст в буфер обмена
            document.execCommand("copy");

            // Удаляем временный элемент textarea
            document.body.removeChild(textArea);

            // Изменяем текст кнопки на "Скопировано"
            this.textContent = "Скопировано";
        });
    });
});
