#!/bin/bash

# Включаем режим отладки
set -x

# Команда для сборки Docker образа
docker build -t storytech-jupyter-notebook -f dockerfile.notebook .

# Проверка статуса предыдущей команды
if [ $? -ne 0 ]; then
  echo "Ошибка при сборке Docker образа."
  exit 1
fi

# Команда для запуска контейнеров с пересборкой
docker compose up -d --build

# Проверка статуса предыдущей команды
if [ $? -ne 0 ]; then
  echo "Ошибка при запуске контейнеров."
  exit 1
fi

echo "Docker образ успешно собран и контейнеры успешно запущены."

# Отключаем режим отладки
set +x
