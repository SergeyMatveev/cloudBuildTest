# Используем официальный базовый образ Python с Docker Hub
FROM python:3.8

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Задаем команду, которая будет выполнена при запуске контейнера
CMD ["python", "main.py"]