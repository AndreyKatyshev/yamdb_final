# Проект YaMDb

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Список категорий (Category) может быть расширен администратором 
(например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.

Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.


### Применённые технологии
- Python 
- Docker
### Адрес сайта
http://158.160.9.75/redoc/
### Пример запроса
http://158.160.9.75/api/v1/titles/

### Заполнение файла .env
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=<имя базы данных>
- POSTGRES_USER=<логин для подключения к базе данных>
- POSTGRES_PASSWORD=<пароль для подключения к БД>
- DB_HOST=<название сервиса (контейнера)>
- DB_PORT=<порт для подключения к БД>

![status badge](https://github.com/andreykatyshev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Автор проекта
Андрей Катышев