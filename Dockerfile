# Используем базовый образ Python
FROM python:3.8

# Устанавливаем переменную окружения для отключения вывода логов Python
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для работы с изображениями
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev

# Создаем рабочую директорию для проекта
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . /app/

# Запускаем команду для запуска Django приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
