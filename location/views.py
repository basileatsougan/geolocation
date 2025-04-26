from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    json_location_data = res.text
    location_data = json.loads(json_location_data)
    
    print('res is: ', res)
    print('\nJSON location data is: ', json_location_data)
    print('\nlocation data is: ', location_data)
    return render(request, 'index.html', {'data': location_data})