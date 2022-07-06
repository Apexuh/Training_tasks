#earthquake_app
import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

response = requests.get(url, headers= {'Accept' : 'application/json'}, params={
	'format':'geojson',
	'starttime':input('Enter the start time'),
	'endtime':input('Enter the end time'),
	'latitude':input('Enter the latitude'),
	'longitude':input('Enter the longitude'),
	'maxradiuskm':input('Enter the max radius in km'),
	'minmagnitude':input('Enter the min magnitude')

	})

#for testing
# response = requests.get(url, headers= {'Accept' : 'application/json'}, params={
# 	'format':'geojson',
# 	'starttime':'2019-01-01',
# 	'endtime':'2019-05-01',
# 	'latitude':'51.51',
# 	'longitude':'-0.12',
# 	'maxradiuskm':'2000',
# 	'minmagnitude':'2'

# 	})

data = response.json()
for i in range(len(data['features'])):
	print(f"{i+1}. Place: {data['features'][i]['properties']['place']}. Magnitude: {data['features'][i]['properties']['mag']}")

	