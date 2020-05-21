# Тестовое задание 3. Агрегатор погодных сервисов
### Задание
>Необходимо написать агрегатор информации о погоде из открытых сервисов.
#
### Введение
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Агрегатор работает с шестью сервисами: [OpenWeather](https://openweathermap.org/api), [Weatherbit](https://www.weatherbit.io/api), [World Weather Online](https://www.worldweatheronline.com/developer/api/), [WeatherAPI](https://www.weatherapi.com/api-explorer.aspx), [AccuWeather](https://developer.accuweather.com/apis), [ClimaCell](https://www.climacell.co/weather-api/). В качестве наиболее универсальных методов формирования запроса выбраны название города и географические координаты. Последние можно получить с помощью вспомогательного метода ```get_coordinates()``` из загруженной базы городов ([источник](openweathermap.org)).<br/><br/>

### Описание методов API

| Метод | Параметры | Возвращаемый результат |
| :--- | :---: | :---: |
| ```get_weather()``` <br/> Вывод информации о погоде в городе | ```**location``` <br/> В качестве ключей словаря можно использовать ```'city'``` – название города (предпочтительно англоязычное), <br/> либо ```'lat', 'lon'``` – широту и долготу  | str \* |
| ```get_services()``` <br/> Список сервисов с которыми работает приложение | – | str \*\* |
| ```get_coordinates()``` <br/> Широта и долгота города | ```city``` <br/> Название города | list \*\*\* |

\* структура вывода функции ```get_weather()``` output is: (конец строки ```'\n'```)
```
Current temperature in <city> is:
...
<temperature>℃ (<service>)
...
More than one city with given name: enter coordinates to specify place   # опционально
```
\*\* структура вывода функции ```get_services()```:
```
...
<service> status is <status>   # <status> может быть "OK" или <response.status_code> или <Error message>
...
```
\*\*\* структура вывода функции ```get_coordinates()```:
```
[<int>, {'lat': <float>,      # первый элемент списка – число городов с одинаковым названием
         'lon': <float>,      # второй – словарь, в который записаны координаты и код страны
         'country': <str>}]   #          первого совпавшего с запросом города из базы
```
