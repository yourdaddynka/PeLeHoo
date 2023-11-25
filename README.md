Пока такое решение. Нужно создать файл ```.env```, 
скопировать туда следующие строки и заполнить пропущенные значения, чтобы подключиться к БД.
Пользователь и база должны существовать

POSTGRES_ENGINE="django.db.backends.postgresql"
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST="localhost"
POSTGRES_PORT=5432
