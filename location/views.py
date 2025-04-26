from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    # To get the user IP ADDRESS
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    # res = requests.get('http://ip-api.com/json/24.48.0.1')
    res = requests.get('http://ip-api.com/json/'+ip_data['ip'])
    json_location_data = res.text
    location_data = json.loads(json_location_data)
    
    print('location data is: ', location_data)
    return render(request, 'index.html', {'data': location_data})