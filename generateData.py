import os
import json
from captionbot import CaptionBot
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning  
from requests.packages.urllib3.exceptions import InsecurePlatformWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

c = CaptionBot()

json_object = {
	'data': {
		'caption': "",
		'filename': "",
		'film-frame': 0
	}
}

fps = 25
stepInSeconds = 3
stepInFrames = fps * stepInSeconds 

frame_files = 0
json_files = 0

for f in os.listdir('data/frames/'):
	parsed = f.split(".")
	if parsed[1] == 'png':
		frame_files += 1
	else:
		json_files += 1

index = json_files + 1

print "Total frames:", str(frame_files)
print "Total JSONs:", str(json_files)
print "To process now:", str(frame_files - json_files)
print "Starting at frame:", str(index)

for i in range(index, frame_files):
	#c.url_caption('your image url here')
	data = c.file_caption('data/frames/' + str(i) + '.png')
	print "Frame " + str(i) + " :: " + data

	json_object['data']['caption'] = data
	json_object['data']['filename'] = 'data/frames/' + str(i) + '.png'
	json_object['data']['film-frame'] = i
	
	os.system('touch data/frames/' + str(i) + ".json")

	with open("data/frames/" + str(i) + ".json", 'r+') as json_data:
		json.dump(json_object, json_data, indent=2)

print "Finished!"