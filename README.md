## **Описание проекта:**
Проект api_yatube - это API социальной сети Yatube построенная на архитектуре Dajngo REST Framework с использованием сериалайзеров, вьюсетов и роутеров.

С помощью api_yatube можно запрашивать данные о постах, группах, комментариях в социальной сети Yatube, а также создавать новые.

Yatube - это социальная сеть для авторов и подписчиков. Пользователи могут подписываться на авторов, оставлять и удалять комментарии к постам, оставлять посты на главной странице и в тематических группах, прикреплять изображения к публикуемым постам.

Этот же проект написаный полностью на Django (frontend+backend) запущен на хостинге PythonAnyWhere по ссылке:

```
http://eve982.pythonanywhere.com/
```

## **Как запустить проект:**
Все команды необходимо выполнять в командной строке Вашего ПК. Первую команду следует выполнять в той локальной папке своего ПК, в которую Вы хотите склонировать проект из стороннего репозитория.
Клонировать репозиторий выполнением следующей команды в командной строке:

```
git clone <сссылка на проект>
```
если Вы используете SSH-подключение, то, вместо <сссылка на проект>, укажите:

```
https://github.com/Eve982/api_final_yatube.git
```
для HTTPS-подключений укажите следующую ссылку:

```
https://github.com/Eve982/api_final_yatube.git
```
Перейти в клонированый проект командой:

```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
Запустить виртуальное окружение:

```
source venv/bin/activate
```
Обновить пакетный менеджер pip во избежание проблем при установке зависимостей приложения:

```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## **Примеры запросов:**

## Примеры работы с API для всех пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

```r
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```

## Примеры работы с API для авторизованных пользователей

- Для создания публикации используем:

```r
POST /api/v1/posts/
```

в body

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Обновление публикации:

```r
PUT /api/v1/posts/{id}/
```

в body

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Частичное обновление публикации:

```r
PATCH /api/v1/posts/{id}/
```

в body

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Частичное обновление публикации:

```r
DEL /api/v1/posts/{id}/
```

Получение доступа к эндпоинту /api/v1/follow/ (подписки) доступен только для авторизованных пользователей.

Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.

```r
GET /api/v1/follow/
```

- Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.
- Пользователи могут изменять(удалять) контент, автором которого они являются.

## Добавить группу в проект нужно через админ панель Django:

после авторизации, переходим в раздел Groups и создаем группы.

```r
admin/
```

- Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:

```r
POST /api/v1/jwt/create/
```

- Передав в body данные пользователя (например в postman):

```json
{
"username": "string",
"password": "string"
}
```

- Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:

```r
Authorization: Bearer {your_token}
```

- Обновить JWT-токен:

```r
POST /api/v1/jwt/refresh/
```

- Проверить JWT-токен:

```r
POST /api/v1/jwt/verify/
```

- Так же в проекте API реализована пагинация (LimitOffsetPagination):

```r
GET /api/v1/posts/?limit=5&offset=0
```


Деплой проекта: http://eve982.pythonanywhere.com

