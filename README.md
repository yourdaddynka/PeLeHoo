Пока такое решение. Нужно создать файл ```.env```, 
скопировать туда следующие строки и заполнить пропущенные значения, чтобы подключиться к БД.
Пользователь и база должны существовать


SECRET_KEY="django-insecure-p@d$v7(og((fs=%eat64ju+f7_8r*)kq+!u@j#y(foiht4w@+1"

POSTGRES_ENGINE="django.db.backends.postgresql"
POSTGRES_DB=""
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_HOST="localhost"
POSTGRES_PORT=5432

DEBUG=True

после этого нужно запустить команды:

```python3 -m venv venv```

```python3 -m pi install --upgrade pip```

```pip install -r requirements.txt```

```python3 manage.py runserver```

После этого по адресу ```127.0.0.1:8000``` должна открыться страница приложения

Можно сделать ```python3 manage.py createsuperuser``` и ввести данные 

для регистрации пользователя-администратора 