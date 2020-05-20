# Тестовое задание 3. Агрегатор погодных сервисов
### Задание
>Необходимо написать агрегатор информации о погоде из открытых сервисов.
#
### Описание API
#

| Метод | Параметры | Возвращаемый результат |
| :--- | :---: | :---: |
| ```get_weather()``` <br/> Вывод информации о погоде в городе | ```**location```<br/>В качестве ключей словаря можно использовать ```'city'``` – название города (предпочтительно англоязычное),<br/>либо ```'lat', 'lon'``` – широту и долготу  | str \* |
| ```get_services()``` <br/> Список сервисов с которыми работает приложение | – | str \*\* |

\* structure of ```get_weather()``` output is: (```'\n'``` as newline)
```
Current temperature in <city> is:
...
<temperature>℃ (<service>)
...
More than one city with given name: enter coordinates to specify place   # optional
```
\*\* structure of ```get_services()``` output is:
```
...
<service> status is <status>   # <status> could be "OK" or <response.status_code> or <Error message>
...
```
