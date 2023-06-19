# Використовуємо базовий образ Python
FROM python:3.9

# Встановлюємо залежності проекту
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt

# Копіюємо весь код проекту в контейнер
COPY . /code/

# Виконуємо команду запуску Django-сервера
CMD ["python", "manage.py", "runserver", "127.0.0.1:8080"]
