# Використовуємо базовий образ Python
FROM python:3.8-slim

# Встановлюємо залежності
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копіюємо додаток у контейнер
COPY . .

# Вказуємо команду для запуску додатку
CMD ["python", "my_app.py"]

# Виділяємо порт
EXPOSE 5000