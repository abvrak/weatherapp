from django.shortcuts import render
import urllib.request
def index(request):
    import json
    import requests

    city = "Lublin"

    api_request = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                    city + '&units=metric&appid=774f08ce17fe66123b6b05f685240b05').read()
    try:
        api = json.loads(api_request)
    except Exception as e:
        api = "Error"
    return render(request, 'index.html', {'api': api})
def about(request):
    return render(request, 'about.html', {})