#### ОПИСАНИЕ КОНЦЕПЦИИ ####

Создание консольного приложения для поиска фильмов по базе данных sakila.
В качестве источника данных будет предоставлена тестовая база данных с
фильмами, которую студентам нужно установить на локальном сервере.
Все введенные поисковые запросы сохраняются в отдельной таблице в отдельной
базе. Проектное приложение позволяет вывести самые популярные запросы по
команде пользователя.

#### ЦЕЛЬ ПРОЕКТА ####

Реализовать сценарии поиска фильмов:
* По ключевому слову находится 10 фильмов.
* По жанру и году находится 10 фильмов.
* По команде выводится список самых популярных запросов, по которым был
поиск.

#### ПРОЦЕСС РАБОТЫ НАД ПРОЕКТОМ ####

1. Установить тестовую базу у себя на локальном сервере и ознакомиться со
структурой таблиц и их содержимым, понять связи и типы данных.
Рекомендуется написать несколько запросов, который выводят фильмы
определенного жанра и фильмы за определенный год.

2. Имея понимание структуры базы и описание сценариев, написать нужные
запросы на SQL. Приготовьте работающие запросы, которые позже вы будете
использовать из приложения на Python.

3. Напишите запросы, которые сохраняют выбранные ключевые слова, по
которым осуществлялся поиск, в отдельную таблицу.

4. Напишите запросы, которые выводят запросы по популярности - наиболее
частые выводятся первыми.

5. После того, как мы убедились, что запросы работают, начинаем
проектировать и разрабатывать приложение на Python и интеграция с базой
данных. Приложение должно запускаться из консоли и работать в
интерактивном режиме, ожидая ввода команд от пользователя. Пользователь
должен вводить команды и получать результаты непосредственно в консоли.
Нужно подумать, какие модули\классы нужны нашему приложению, как
разнести логику по разным модулям\классам\функциям. Например, всю
работу с базой данных можно реализовать отдельным модулем, который
будет использоваться из модуля работы с пользователем (считывание команд
с клавиатуры). Также можно вынести отображение результатов в отдельный
модуль.

#### ПРЕЗЕНТАЦИЯ РЕЗУЛЬТАТОВ ####

Презентовать выводы по реализации проекта, продемонстрировать работу
консольного приложения.
5 минут презентация и вопросы/ответы от преподавателя.