# nik-test-task
Тестовое задание для НИК


Описание

Требуется, получив список проектов через API Github по подстроке поиска, вернуть их пользователю в формате JSON, предварительно сохранив результаты в БД.


Сценарий

1. Пользователь определяет подстроку поиска проектов на Gitlab;
2. Подстрока поиска передается в запрос на получение списка проектов https://gitlab.com/api/v4/projects/?search=<подстрока>;
3. API Gitlab возвращает список найденных проектов;
4. Из каждого найденого проекта выбираются атрибуты: id, name, description и last_activity_at;
5. Полученный список проектов сохраняется в локальную БД (SQLite);
6. Каждая созданная запись в БД должна получить атрибут created_at, соответствующий дате создания записи в таблице;
7. Пользователю возвращается ответ в формате JSON, содержащий искомые проекты, полученные из локальной БД.
