<h1>Сравнение Postgres и Mongo</h1>
<h2>Генерирование данных для тестов</h2>
<p>Для генерации данных используемых в дальнейшем для тестирования используется 
скрипт <code>generate_data.py</code>. После выполнения в папках postgres и 
mongo создаются файлы <code>users.csv</code> (файл с пользователями), 
<code>movies.csv</code> (файл с фильмами), 
<code>likes.csv</code> (файл с лайками).</p>
<h2>Тестирование Mongo</h2>
<p>Для тестирования Mongo необходимо переменную окружения <code>USER_CLASS</code>
установить в значение равное <code>MongoUser</code>.
Далее собираем проект командой <code>docker-compose up --build</code>.
Ожидаем пока отработает контейнер <code>mongo_importer</code>, который импортирует
данные из файлов .csv в базу Mongo и индексирует ее. После завершения
индексации и импорта переходим по адресу Locust и начинаем тестирование.</p>
<h2>Тестирование Postgres</h2>
<p>Для тестирования postgres необходимо переменной окружения <code>USER_CLASS</code>
присвоить значение <code>PostgresUser</code>. Собираем проект <code>docker-compose up --build</code>.
После окончания импорта данных можно начинать тестирование в Locust.</p>
<h2>Результаты тестирования</h2>
<p>Подробные результаты тестирования описаны в папке results. Тестирование 
проводилось под нагрузкой в 100 пользователей. По результатам запись и чтение 
данных на Mongo проводятся быстрее, с агрегационными запросами Postgres
справляется лучше. Так как скорость чтения данных для поставленных задач
приоритетный параметр целесообразно использовать Mongo.</p>
