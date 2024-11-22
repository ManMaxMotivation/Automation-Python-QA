# СПРИНТ 11

## Автоматизация чек-листа для поля `name` в запросе на создание набора в Яндекс Прилавке с помощью API Яндекс Прилавка.

Яндекс Прилавок это учебное web-приложение для практики работы с API, SQL.

✨Документация API Прилавка (apiDoc) ✨

[![N|Solid](https://i.ibb.co/rQ1hk93/1.jpg)](https://nodesource.com/products/nsolid)
[![N|Solid](https://i.ibb.co/mBGRX0c/2.jpg)](https://nodesource.com/products/nsolid)
- Язык приложения — `JavaScript`.
- Доступ к приложению по протоколу `HTTP 1.1`.
- Документация к приложению осуществляется с помощью модуля `apiDoc`.
- Приложение использует базу данных — `PostgreSQL`.

### Требования

- Для запуска тестов должны быть установлены пакеты `pytest` и `requests`.
- Запуск всех тестов выполняется командой `pytest`.

### Чек-лист проверок

| №  | Описание                                                                     | ОР                                                                            |
|----|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 1  | Допустимое количество символов (1): `kit_body = { "name": "a" }`             | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 2  | Допустимое количество символов (511): тестовое значение под таблицей         | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 3  | Количество символов меньше допустимого (0): `kit_body = { "name": "" }`      | <br/>Код ответа — 400                                                         |
| 4  | Количество символов больше допустимого (512): тестовое значение под таблицей | <br/>Код ответа — 400                                                         |
| 5  | Разрешены английские буквы: `kit_body = { "name": "QWErty" }`                | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 6  | Разрешены русские буквы: `kit_body = { "name": "Мария" }`                    | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 7  | Разрешены спецсимволы: `kit_body = { "name": ""№%@"," }`                     | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 8  | Разрешены пробелы: `kit_body = { "name": " Человек и КО " }`                 | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 9  | Разрешены цифры: `kit_body = { "name": "123" }`                              | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 10 | Параметр не передан в запросе: `kit_body = {}`                               | <br/>Код ответа — 400                                                         |
| 11 | Передан другой тип параметра (число): `kit_body = { "name": 123 }`           | <br/>Код ответа — 400                                                         |

#### Тестовые значения для проверок №2 и №4
Допустимое количество символов (511)
```py
kit_body = { "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC" }
```
Количество символов больше допустимого (512)
```py
kit_body = { "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD" }
```

### Шаги выполнения проекта

1. Написать `POST`-запрос на создание нового пользователя и сохранение токена авторизации authToken.
2. Написать `POST`-запрос на создание личного набора для этого пользователя. Учесть передачу заголовка Authorization.
3. Написать функции для проверки позитивных и негативных сценариев чек-листа.
4. Запустить автотест.
5. Упаковать папку с файлами `configuration.py`, `data.py`, `sender_stand_request.py`, `create_kit_name_kit_test.py`, `README.md`, `.gitignore` в ZIP-архив.

> #### Создание пользователя
> Тип запроса – `POST`.
> Эндпоинт – `/api/v1/users`.
> ###### Успешное создание учётной записи пользователя
> ```xml
> HTTP/1.1 201 Created
> {
>    authToken: 'jknnFApafP4awfAIFfafam2fma'
> }
> ```

> #### Создание набора внутри конкретной карточки или пользователя
> Тип запроса – `POST`.
> Эндпоинт – `/api/v1/kits`.
> ###### Заголовок для получения наборов, созданных пользователем
> ```xml
> {
>    "Content-Type": "application/json",
>    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
> }
> ```

### Стек для выполнения проекта
* PyCharm
* GitHub
* requests
* pytest