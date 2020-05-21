
import requests as web
import json

# reading urls and keys for our services
with open("services.json") as file:
    services = json.load(file)

# reading large database of ~209500 cities
# source: openweathermap.org
with open("city.list.json", encoding="utf8") as file:
    cities = json.load(file)

# list of active services: default - all,
# call get_services() to actualize status
services_log = []
for s in services:
    services_log.append([s['name'], s['short_name']])

# using cities database to find coordinates by city name
def get_coordinates(city):
    global cities
    # first element is the number of cities with the same name
    coordinates = [0]
    try:
        for i in cities:
            if i['name'] == city:
                if coordinates[0] > 0:
                    # check if there are entries with very close coordinates
                    for j in coordinates:
                        if type(j) is int:
                            continue
                        # and will add only if they are not
                        if int(i["coord"]["lat"]) != int(j["lat"]) and \
                                int(i["coord"]["lon"]) != int(j["lon"]):
                            coordinates[0] += 1
                            # 'country' field is not used in this version,
                            # but could be helpful
                            coordinates.append({"lat": i["coord"]["lat"],
                                                "lon": i["coord"]["lon"],
                                                "country": i["country"]})
                            break
                else:
                    coordinates[0] += 1
                    coordinates.append({"lat": i["coord"]["lat"],
                                        "lon": i["coord"]["lon"],
                                        "country": i["country"]})
        return coordinates
    except Exception as e:
        return e.args[0]

# OpenWeather status check
def test_OW():
    global services
    url, par = services[0]['url_city'], services[0]['par_city']
    par['q'] = "London"
    try:
        return web.get(url, params=par).status_code
    except Exception as e:
        # just in case
        return e.args[0]

# OpenWeather call for temperature
def get_OW(**location):
    global services
    answer = []
    # we could use city name for API call
    if "city" in location.keys():
        # in most services must use varying url and params for
        # different type of calls
        url, par = services[0]['url_city'], services[0]['par_city']
        # check for multiple cities with one name
        # in next version better check it externally
        cities_log = get_coordinates(location['city'])
        if cities_log[0] > 1:
            answer.append(cities_log[0])
        par['q'] = location['city']
    # or we could use latitude and longitude for API call
    elif "lat" and "lon" in location.keys():
        url, par = services[0]['url_coord'], services[0]['par_coord']
        par['lat'] = location['lat']
        par['lon'] = location['lon']
    else:
        # RTFM if got this
        raise AttributeError
    try:
        response = web.get(url, params=par).json()
        # temperature is always the first element of list to return
        answer.insert(0, float(response['main']['temp']))
        return answer
    except Exception as e:
        return e.args[0]

# Weatherbit status check
def test_WB():
    global services
    url, par = services[1]['url_city'], services[1]['par_city']
    par['city'] = "London"
    try:
        return web.get(url, params=par).status_code
    except Exception as e:
        return e.args[0]

# Weatherbit call for temperature
def get_WB(**location):
    global services
    answer = []
    if "city" in location.keys():
        url, par = services[1]['url_city'], services[1]['par_city']
        cities_log = get_coordinates(location['city'])
        if cities_log[0] > 1:
            answer.append(cities_log[0])
        par['city'] = location['city']
    elif "lat" and "lon" in location.keys():
        url, par = services[1]['url_coord'], services[1]['par_coord']
        par['lat'] = location['lat']
        par['lon'] = location['lon']
    else:
        raise AttributeError
    try:
        response = web.get(url, params=par).json()
        answer.insert(0, float(response['data'][0]['temp']))
        return answer
    except Exception as e:
        return e.args[0]

# World Weather Online status check
def test_WWO():
    global services
    url, par = services[2]['url'], services[2]['par']
    par['q'] = "London"
    try:
        return web.get(url, params=par).status_code
    except Exception as e:
        return e.args[0]

# World Weather Online call for temperature
def get_WWO(**location):
    global services
    # this one has same url and params for any call, only 'q' field varies
    url, par = services[2]['url'], services[2]['par']
    answer = []
    if "city" in location.keys():
        cities_log = get_coordinates(location['city'])
        if cities_log[0] > 1:
            answer.append(cities_log[0])
        par['q'] = location['city']
    elif "lat" and "lon" in location.keys():
        par['q'] = ','.join([location['lat'], location['lon']])
    else:
        raise AttributeError
    try:
        response = web.get(url, params=par).json()
        answer.insert(0, float(response['data']['current_condition'][0]['temp_C']))
        return answer
    except Exception as e:
        return e.args[0]

# WeatherAPI status check
def test_WAPI():
    global services
    url, par = services[3]['url'], services[3]['par']
    par['q'] = "London"
    try:
        return web.get(url, params=par).status_code
    except Exception as e:
        return e.args[0]

# WeatherAPI call for temperature
def get_WAPI(**location):
    global services
    # this one has same url and params for any call, only 'q' field varies
    url, par = services[3]['url'], services[3]['par']
    answer = []
    if "city" in location.keys():
        cities_log = get_coordinates(location['city'])
        if cities_log[0] > 1:
            answer.append(cities_log[0])
        par['q'] = location['city']
    elif "lat" and "lon" in location.keys():
        par['q'] = ','.join([location['lat'], location['lon']])
    else:
        raise AttributeError
    try:
        response = web.get(url, params=par).json()
        answer.insert(0, float(response['current']['temp_c']))
        return answer
    except Exception as e:
        return e.args[0]

# AccuWeather status check
# only 50 calls/day
def test_AW():
    global services
    url = services[4]['url_ID'].format(location_ID="328328")
    par = services[4]['par_ID']
    try:
        return web.get(url, params=par).status_code
    except Exception as e:
        return e.args[0]

# AccuWeather call for temperature
def get_AW(**location):
    global services
    # this service only use call by 'location_ID'
    url, par = services[4]['url_search'], services[4]['par_search']
    answer = []
    if "city" in location.keys():
        cities_log = get_coordinates(location['city'])
        if cities_log[0] > 1:
            answer.append(cities_log[0])
        par['q'] = location['city']
    elif "lat" and "lon" in location.keys():
        raise KeyError
    else:
        raise AttributeError
    try:
        # at first we call for location_ID by city name
        response = web.get(url, params=par).json()
        url = services[4]['url_ID'].format(location_ID=response[0]['Key'])
        par = services[4]['par_ID']
        # then we use it for temperature call
        response = web.get(url, params=par).json()
        answer.insert(0, float(response[0]['Temperature']['Metric']['Value']))
        return answer
    except Exception as e:
        return e.args[0]

# ClimaCell status check
def test_CC():
    global services
    url, par = services[5]['url_coord'], services[5]['par_coord']
    par['lat'] = "51.51334"; par['lon'] = "-0.08901"
    try:
        return web.get(url, params=par).status_code
    except Exception as e:
        return e.args[0]

# ClimaCell call for temperature
def get_CC(**location):
    global services
    # this service only use latitude and longitude
    url, par = services[5]['url_coord'], services[5]['par_coord']
    answer = []
    if "lat" and "lon" in location.keys():
        par['lat'], par['lon'] = location['lat'], location['lon']
    elif "city" in location.keys():
        # so if we have only city name, then check cities database
        cities_log = get_coordinates(location['city'])
        if cities_log[0] > 1:
            answer.append(cities_log[0])
        if len(cities_log) > 1:
            par['lat'], par['lon'] = cities_log[1]['lat'], cities_log[1]['lon']
        else:
            # we hadn't find a city if got here
            raise ValueError
    else:
        raise AttributeError
    try:
        response = web.get(url, params=par).json()
        answer.insert(0, float(response['temp']['value']))
        return answer
    except Exception as e:
        return e.args[0]


# (second) method to get list of all services we work with and corresponding statuses
def get_services():
    global services
    global services_log
    report = []
    test_t = "{} status is {}"
    for s in services:
        # calling all corresponding test functions
        res = globals()['test_' + s['short_name']]()
        # got we a status_code or an error message here?
        if type(res) is int:
            if res == 200:
                report.append(test_t.format(s['name'], "OK"))
            else:
                # type status_code to the report
                report.append(test_t.format(s['name'], res))
                # and remove this entry from the list of active services
                services_log.remove([s['name'], s['short_name']])
        else:
            # type an error message to the report
            report.append(test_t.format(s['name'], res.args[0]))
            # and remove this entry from the list of active services
            services_log.remove([s['name'], s['short_name']])
    return report


# (first) method to get list of temperatures from all active services
def get_weather(**location):
    global services
    global services_log
    flag = False
    weather_t_out = "{:.1f}\u2103 ({})"
    if "city" in location.keys():
        # just a header of the report
        report = ["Current temperature in {} is:".format(location['city'])]
    # maybe for next version we could write function to search
    # location name by coordinates? ehm.. not this time.
    elif "lat" and "lon" in location.keys():
        report = ["Current temperature in {} is:".
                      format(', '.join([location['lat'], location['lon']]))]
    else:
        # RTFM if got this
        raise AttributeError
    # here we cycle only through active services
    for s in services_log:
        if "city" in location.keys():
            try:
                # calling all corresponding get functions
                res = globals()['get_' + s[1]](city=location['city'])
            except ValueError:
                # are you sure in your city name?
                report.append("Unknown city")
        elif "lat" and "lon" in location.keys():
            try:
                res = globals()['get_' + s[1]](lat=location['lat'],
                                               lon=location['lon'])
            except KeyError:
                report.append(s[0] + " can't use this endpoint")
                continue
        if type(res) is list and len(res) > 1 and not flag:
            # we got multiple cities with one name
            flag = True
        try:
            # here the temperatures finally
            report.append(weather_t_out.format(res[0], s[0]))
        except ValueError:
            # are you sure in your city name?
            report.append("Unknown city")
        except TypeError:
            # probably we lost connection or exceed call limit
            # call get_status() to know
            report.append("No access, please check the status of " + s[0])
    if flag:
        # just a note about multiple cities with one name
        report.append("More than one city with given name: enter "
                      "coordinates to specify place")
    return report
