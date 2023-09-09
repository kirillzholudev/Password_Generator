document.addEventListener("DOMContentLoaded", function() {
    // Находим все кнопки "Скопировать"
    var copyButtons = document.querySelectorAll(".copy-button");
    var activeCopyButton = null; // Текущая активная кнопка "Скопировать"

    // Добавляем обработчик события на каждую кнопку
    copyButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Если есть активная кнопка "Скопировать", сбрасываем ее состояние
            if (activeCopyButton !== null) {
                activeCopyButton.textContent = "Скопировать";
            }

            // Если текущая кнопка не активна, устанавливаем ее активной
            if (activeCopyButton !== this) {
                activeCopyButton = this;
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

                // Изменяем текст текущей кнопки на "Скопировано"
                this.textContent = "Скопировано";
            } else {
                // Если текущая кнопка уже активна, сбрасываем активное состояние
                activeCopyButton = null;
                this.textContent = "Скопировать"; // Возвращаем текст "Скопировать"
            }
        });
    });
});
