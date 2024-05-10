ADS Online
Описание:
Данная работа представляет собой backend-часть для сайта объявлений (реализация с помощью Django Rest Framework и JWT).

Frontend часть готова (реализация - React)

Функционал:
Авторизация и аутентификация пользователей.
Распределение ролей между пользователями (пользователь и админ).
CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
Под каждым объявлением пользователи могут оставлять отзывы.
В заголовке сайта можно осуществлять поиск объявлений по названию.

Технологии:
Python
Django
Django REST framework
psycopg2-binary
JWT
DRF-YASG
CORS
Docker
Docker Compose

Запуск проекта
Локально:

Клонировать файлы проекта с GitHub репозитория:
https://github.com/MochalovaES/bulletin_board/

Создать виртуальное окружение:
python -m venv venv
Активировать виртуальное окружение:
venv/Scripts/activate (Windows)
source venv/bin/activate (Linux, MacOS)
Установить зависимости:
pip install -r requirements.txt
Создать файл .env c переменными окружения.
Добавить в файл настройки, как в .env.sample и заполнить их.
Создайте базу данных, выполните python skymarket/manage.py migrate.
Заполнить базу данных:
python skymarket/manage.py loaddata skymarket/fixtures/users.json
python skymarket/manage.py loaddata skymarket/fixtures/ad.json
python skymarket/manage.py loaddata skymarket/fixtures/comments.json
Создайте администратора, выполните python skymarket/manage.py csu.
Запустите сервер разработки, выполните python skymarket/manage.py runserver.

Работа с сервисом через Postman

1. Получить токен

POST: http://localhost:8000/users/token/
body: {
"email": <электронная почта>,
"password": <пароль>
}

2. Подключить авторизацию по токену

3. Эндпоинты:

- Создание объявления

POST: http://localhost:8000/ads/
body: {
"title": "Компьютер недорого",
"price": 10000,
"description": "Компьютер недорого"
}
*image, created_at - необязательны для заполнения

- Просмотр детальной информации об объявлении

GET: http://localhost:8000/ads/<id_объявления>/

- Просмотр всех объявлений

GET: http://localhost:8000/ads/

- Редактирование объявления

PUT: http://localhost:8000/ads/<id_объявления>/
PATCH: http://localhost:8000/ads/<id_объявления>/

- Удаление объявления

DELETE: http://localhost:8000/ads/<id_объявления>/

- Просмотр отзывов определенного объявления

GET: http://localhost:8000/ads/<id_объявления>/comments

- Просмотр конкретного отзыва определенного объявления

GET: http://localhost:8000/ads/<id_объявления>/comments/<id_отзыва>/

- Изменение отзыва

PUT: http://localhost:8000/ads/<id_объявления>/comments/<id_отзыва>/
PATCH: http://localhost:8000/ads/<id_объявления>/comments/<id_отзыва>/

- Удаление отзыва

DELETE: http://localhost:8000/ads/<id_объявления>/comments/<id_отзыва>/

Просмотр документации
Swagger
http://localhost:8000/swagger/

Redoc
http://localhost:8000/redoc/

Запуск проекта через docker-compose:
При необходимости установите Docker и Docker Compose на компьютер с помощью
инструкции https://docs.docker.com/engine/install/
Cклонируйте репозиторий себе на компьютер
Создайте файл .env и заполните его, используя образец из файла .env.sample
Соберите образ с помощью команды docker-compose build
Запустите контейнеры с помощью команды docker-compose up
Сборка и запуск контейнера в фоновом режиме: docker-compose up -d --build

Техническое задание:
Этап I. Настройка Django-проекта.
Этап II. Создание модели юзера. Настройка авторизации и аутентификации.
Этап III. Описание моделей объявлений и отзывов.
Этап IV. Создание views и эндпоинтов.
Этап V. Определение permissions к views.
