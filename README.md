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

После запуска виртуального сервера можно протестировать работоспособность проекта.

