# Тестовое задание 3. Агрегатор погодных сервисов
### Задание
>Необходимо написать агрегатор информации о погоде из открытых сервисов.
#
### Введение
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Агрегатор работает с шестью сервисами: [OpenWeather](https://openweathermap.org/api), [Weatherbit](https://www.weatherbit.io/api), [World Weather Online](https://www.worldweatheronline.com/developer/api/), [WeatherAPI](https://www.weatherapi.com/api-explorer.aspx), [AccuWeather](https://developer.accuweather.com/apis), [ClimaCell](https://www.climacell.co/weather-api/). В качестве наиболее универсальных конечных точек различных API выбраны название города и географические координаты. Последние можно получить по названию города с помощью вспомогательного метода ```get_coordinates()``` из загруженной базы городов ([источник](openweathermap.org)). Этот же метод обрабатывает совпадающие названия городов.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Вывод погоды от разных сервисов унифицирован с помощью шаблона.<br/><br/>

### Описание методов API

| Метод | Параметры | Возвращаемый результат |
| :--- | :---: | :---: |
| ```get_weather()``` <br/> Вывод информации о погоде в городе | ```**location``` <br/> В качестве ключей словаря можно использовать ```'city'``` – название города (предпочтительно англоязычное), <br/> либо ```'lat', 'lon'``` – широту и долготу  | str \* |
| ```get_services()``` <br/> Список сервисов с которыми <br/> работает приложение, проверка доступности сервисов | – | str \*\* |
| ```get_coordinates()``` <br/> Широта и долгота города | ```city``` <br/> Название города | list \*\*\* |

\* структура вывода функции ```get_weather()``` output is: (конец строки ```'\n'```)
```
Current temperature in <city> is:
<temperature>℃ (<service>)
···                                                                      # количество строк согласно 
···                                                                      #  количеству активных сервисов
More than one city with given name: enter coordinates to specify place   # опционально
```
\*\* структура вывода функции ```get_services()```:
```
<service> status is <status>   # <status> может быть "OK" или <response.status_code> или <Error message>
···                            # количество строк согласно общему количеству сервисов
```
\*\*\* структура вывода функции ```get_coordinates()```:
```
[<int>, {'lat': <float>,          # первый элемент списка – число городов с одинаковым названием
         'lon': <float>,          # второй и последующие – словари, в которые записаны координаты и коды
         'country': <str>}, ...]  #                        страны совпавших с запросом городов из базы
```
<br/>

### Примеры
```
>>> get_services()
OpenWeather status is OK
Weatherbit status is OK
World Weather Online status is OK
WeatherAPI status is OK
AccuWeather status is OK
ClimaCell status is OK

>>> get_weather(city="Yekaterinburg")
Current temperature in Yekaterinburg is:
12.0℃ (OpenWeather)
12.5℃ (Weatherbit)
12.0℃ (World Weather Online)
12.0℃ (WeatherAPI)
12.9℃ (AccuWeather)
14.0℃ (ClimaCell)

>>> get_coordinates("Vienna")
[8, {'lat': 48.208488, 'lon': 16.37208, 'country': 'AT'}, 
    {'lat': 33.018742, 'lon': -88.191971, 'country': 'US'}, 
    ...]

>>> get_weather(lat="48.208488", lon="16.37208")
Current temperature in 48.208488, 16.37208 is:
18.0℃ (OpenWeather)
18.8℃ (Weatherbit)
13.0℃ (World Weather Online)
13.0℃ (WeatherAPI)
AccuWeather can't use this endpoint
18.0℃ (ClimaCell)
```
