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
unicodes = [u"\ud83d\ude20", u"\ud83d\ude10", u"\ud83d\ude01", u"\ud83d\ude2f", u"\ud83d\ude2d"]
replacements = ["angry", "neutral", "happy", "hushed", "sad"]
parsed = None

#Open .json files and parse them and generate new frame with subs
for j in range(json_files):
	with open("data/frames/" + str(j+1) + ".json", 'r') as json_data:
		data = json.load(json_data)
		caption = data['data']['caption']
		#remove and replace any emoji contained in the caption string with it's correspondent word     
		for i in range(len(unicodes)):
			if unicodes[i].encode('utf-8') in caption.encode('utf-8'):
				caption = caption.encode('ascii', 'ignore')
				caption += replacements[i]
				caption = caption.split(" .")
				caption = caption[0] + caption[1]
		
		startSplit_result = ""

		#Check for this particular (UNIQUE) caption.ai phrase and add a "DOT"
		if caption == "I think this may be inappropriate content so I won't show it":
			caption = "inappropriate content!"
			caption += "."
			startSplit_result = caption

		#Remove starting phrases given by captionbot.ai
		for i in startingPhrases:
			if caption.startswith(i):
				parsed = caption.split(i)
				startSplit_result = parsed[1]

		#Check for any extra dot chars in the phrase
		#The captions with emotions had their "dots" removed
		#but the rest still have "dots", the following if statements
		#removes these.
		adjustmentSplit = ""
		if "." in startSplit_result:
			parsed = startSplit_result.split(".")
			adjustmentSplit = parsed[0]
		else:
		# 	parsed = parsed[0]
			adjustmentSplit = startSplit_result

	#Generate frame
	imgX = 640
	imgY = 480
	fontname = "data/font/DejaVuSans.ttf"
	fontsize = 30   
	font = ImageFont.truetype(fontname, fontsize)

	img = Image.new('RGB', (imgX, imgY))
	d = ImageDraw.Draw(img)
	lines = textwrap.wrap(adjustmentSplit, width=35)
	y_text = imgY - (imgY/5)

	for line in lines:
	    width, height = font.getsize(line)
	    d.text(((imgX - width) / 2, y_text), line, font=font, fill=(220, 220, 220)) #fill=(242, 239, 96)
	    y_text += height

	print j+1, " | ", adjustmentSplit
	img.save("data/out/" + str(j+1) + ".png")