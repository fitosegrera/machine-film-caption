import Image
import ImageDraw
import ImageFont
import json
import textwrap
import os

#Check how many frames and .json files in the frames folder
frame_files = 0
json_files = 0
for f in os.listdir('data/frames/'):
	parsed = f.split(".")
	if parsed[1] == 'png':
		frame_files += 1
	else:
		json_files += 1

#Possible starting phrases given by captionbot.ai
startingPhrases = ["I am not really confident, but I think it's", "I think it's"]
parsed = None

#Open .json files and parse them and generate new frame with subs
for j in range(json_files):
	with open("data/frames/" + str(j+1) + ".json", 'r') as json_data:
		data = json.load(json_data)
		caption = data['data']['caption']
		print caption
		for i in startingPhrases:
			if caption.startswith(i):
				parsed = caption.split(i)
				parsed = parsed[1].split(".")

	#Generate frame
	imgX = 640
	imgY = 480
	fontname = "data/font/ag-foreigner-roman-medium.ttf"
	fontsize = 30   
	font = ImageFont.truetype(fontname, fontsize)

	img = Image.new('RGB', (imgX, imgY))
	d = ImageDraw.Draw(img)
	lines = textwrap.wrap(parsed[0], width=35)
	y_text = imgY - (imgY/4)

	for line in lines:
	    width, height = font.getsize(line)
	    d.text(((imgX - width) / 2, y_text), line, font=font, fill=(242, 239, 96))
	    y_text += height
	    
	img.save("data/out/" + str(j+1) + ".png")