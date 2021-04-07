<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/SergDinamo14/app_access_with_Face_Recognition?style=for-the-badge"> <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/SergDinamo14/app_access_with_Face_Recognition?style=for-the-badge"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/SergDinamo14/app_access_with_Face_Recognition?style=for-the-badge">

# Система обеспечения доступа к программным компонентам за счёт классификации лиц с использованием нейронных сетей
 
Система распознавания лиц при помощи нейронной сети. Данная система нацелена на обеспечение безопасности необходимых программ и компонентов за счёт классификации лиц и проверки доступа. Основным назначением разработки системы распознавания лиц является осуществления безопасного доступа к определённым программам или компонентам.

## Структура проекта
Система состоит из 3 частей:
1. database_connector - модуль по взаимодействию с базой данных
2. gui - приложение, которое необходимо установить конечному пользователю
3. neural_network - модуль по взаимодействию с нейронной сетью

## Установка
### Модуль по взаимодействию с базой данных
1. Необходимо развернуть сервер с базой данных PostgreSQL. Подробне в сможете найти [здесь](https://postgrespro.ru/docs/postgresql/10/server-start).
2. Создать необходимые таблицы при помощи [скрипта](https://github.com/SergDinamo14/app_access_with_Face_Recognition/blob/main/database%20connector/db_scripts/create_tables.sql).
3. Настроить [конфигурационный файл](https://github.com/SergDinamo14/app_access_with_Face_Recognition/blob/main/database%20connector/config/config.py) (ввести свои данные).
4. Запустить модуль: **python main.py**

### Пользовательское приложение

### Модуль по взаимодействию с нейронной сетью

## Авторы
* [Голышев Илья](https://github.com/golyshevilya)
* [Туркин Сергей] (https://github.com/SergDinamo14)
* [Лащенов Евгений](https://github.com/golyshevilya)
* [Цепцов Даниил](https://github.com/golyshevilya)
