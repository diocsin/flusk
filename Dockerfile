# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы и папки приложения в контейнер
COPY . .

EXPOSE 5000
# Определяем команду, которая будет запускаться при запуске контейнера
CMD ["python", "main.py"]