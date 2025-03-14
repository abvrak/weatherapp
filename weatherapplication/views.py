from django.shortcuts import render
import urllib.request
import json
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        try:
            api_request = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                                 city + '&units=metric&appid=774f08ce17fe66123b6b05f685240b05').read()
            api = json.loads(api_request)
        except Exception as e:
            api = "Error"

        weather_descriptions = {
            "Clouds": "The sky is filled with clouds, which might indicate changing weather conditions or potential rain.",
            "Clear": "The sky is completely clear, providing sunshine and excellent visibility throughout the day.",
            "Mist": "Light mist is settling in, reducing visibility and creating a calm, cool atmosphere.",
            "Smoke": "There's smoke in the air, possibly due to nearby fires, impacting air quality and visibility.",
            "Haze": "A hazy layer of moisture or pollution is affecting the visibility, giving the surroundings a soft, unclear appearance.",
            "Dust": "Winds are stirring up dust, which may reduce visibility and create an overall dry atmosphere.",
            "Fog": "Dense fog is present, making it difficult to see very far ahead and potentially hazardous for travel.",
            "Sand": "Sand is blowing in the air, likely due to a desert wind, reducing visibility and making the air feel gritty.",
            "Ash": "Ash from a nearby volcanic eruption is spreading through the air, reducing visibility and air quality.",
            "Squall": "A sudden squall is hitting, bringing a brief but intense burst of wind and rain.",
            "Tornado": "A tornado warning is in effect, as a rotating column of air is causing potentially dangerous conditions.",
            "Snow": "Snow is gently falling, covering the ground and creating a winter wonderland, but also affecting travel conditions.",
            "Rain": "Light to moderate rain is falling, soaking the ground and providing much-needed moisture.",
            "Drizzle": "A light drizzle is occurring, with tiny raindrops falling steadily, creating a wet, overcast day.",
            "Thunderstorm": "A thunderstorm is underway, with frequent lightning, thunder, and heavy rain, possibly causing temporary disruptions."
        }

        weather_main = api['weather'][0]['main']
        category_description = weather_descriptions.get(weather_main)

        return render(request, 'index.html', {'api': api, 'city': city, 'category_description': category_description}, )
    else:
        try:
            city = "Warsaw"
            api_request = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                                 city + '&units=metric&appid=774f08ce17fe66123b6b05f685240b05').read()
            api = json.loads(api_request)
        except Exception as e:
            api = "Error"

        weather_descriptions = {
            "Clouds": "The sky is filled with clouds, which might indicate changing weather conditions or potential rain.",
            "Clear": "The sky is completely clear, providing sunshine and excellent visibility throughout the day.",
            "Mist": "Light mist is settling in, reducing visibility and creating a calm, cool atmosphere.",
            "Smoke": "There's smoke in the air, possibly due to nearby fires, impacting air quality and visibility.",
            "Haze": "A hazy layer of moisture or pollution is affecting the visibility, giving the surroundings a soft, unclear appearance.",
            "Dust": "Winds are stirring up dust, which may reduce visibility and create an overall dry atmosphere.",
            "Fog": "Dense fog is present, making it difficult to see very far ahead and potentially hazardous for travel.",
            "Sand": "Sand is blowing in the air, likely due to a desert wind, reducing visibility and making the air feel gritty.",
            "Ash": "Ash from a nearby volcanic eruption is spreading through the air, reducing visibility and air quality.",
            "Squall": "A sudden squall is hitting, bringing a brief but intense burst of wind and rain.",
            "Tornado": "A tornado warning is in effect, as a rotating column of air is causing potentially dangerous conditions.",
            "Snow": "Snow is gently falling, covering the ground and creating a winter wonderland, but also affecting travel conditions.",
            "Rain": "Light to moderate rain is falling, soaking the ground and providing much-needed moisture.",
            "Drizzle": "A light drizzle is occurring, with tiny raindrops falling steadily, creating a wet, overcast day.",
            "Thunderstorm": "A thunderstorm is underway, with frequent lightning, thunder, and heavy rain, possibly causing temporary disruptions."
        }

        weather_main = api['weather'][0]['main']
        category_description = weather_descriptions.get(weather_main)

        return render(request, 'index.html', {'api': api, 'city': city, 'category_description': category_description}, )

def about(request):
    return render(request, 'about.html', {})