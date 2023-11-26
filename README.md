<h1>Library manager django app</h1>

<h3>Приложение позволяет:</h3>
<ul>
<li>добавлять книги в библиотеку</li>
<li>использовать поиск по имени книги</li>
<li>смотреть информацию по всем книгам и по выборке из поиска</li>
<li>добавлять пользователей</li>
</ul>

<h3>Для работы в Docker:</h3>
<h3>Изменить строчки в settings.py:</h3>
<ul>
<li>DATABASES - HOST</li>
<li>REDIS_HOST</li>
</ul>
<p>комментарии в коде</p>
<h3>Для работы с Celery и Redis:</h3>
<p>
docker run -d -p 6379:6379 redis<br>
cd library_test_work<br>
celery -A send_greeting worker -l info
</p>

