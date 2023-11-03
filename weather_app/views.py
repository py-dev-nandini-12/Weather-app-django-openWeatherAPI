from datetime import datetime

from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

# Create your views here.


def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=cb3c8ed36d1b7fffd4d77f827b96f5e8').read()
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        # getting the current time
        current_time = datetime.now()
        # formatting the time using directives, it will take this format Day, Month Date Year, Current Time
        formatted_time = current_time

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure']) + "hPa",
            "humidity": str(list_of_data['main']['humidity']) + "%",
            'main': str(list_of_data["weather"][0]['main']),
            'description': str(list_of_data["weather"][0]['description']),
            'icon': list_of_data["weather"][0]['icon'],
            'city': city,
            'time': formatted_time
        }

        # if the request method is GET empty the dictionary
    else:
        data = {}
    return render(request, "index.html", data)