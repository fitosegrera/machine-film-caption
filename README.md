# machine-film-caption

##INSTRUCTIONS

####Setup the Project

The film and frames and outputs are not included in this repository due to file-size issues. You will have to download the desired film by your own means.

[film-files]()

in your data directory create the following folders: 

	data/film
	data/frames
	data/out
	data/out/full

The film files, meaning the .mp4 for the film and the audio file (.mp3), should be stored in the data/film directory. Everything else is generated by following the steps bellow.

####Saving the Frames

The script saveFrames.py calls ffmpeg as a subprocess in order to extract the desired frames from the movie. The film is stored on a directory named data/film, the extracted frames are rendered at data/frames.  

	ffmpeg -i data/film/Dziga-Vertov-Man-With-A-Movie-Camera.mp4 -vf fps=1/3 data/frames/$kino%01d.png

####Generating the Data

The script generateData.py will take each saved frame from the film and submit it to the captionbot.ai API. The returned data is then saved on a .json file in the path data/frames/*.json

The json looks like this. One json file per frame:

	{
	  	"data": {
		    "caption": "I think it's a picture of a sign. ", 
		    "film-frame": 2, 
		    "filename": "data/frames/2.png"
	  	}
	}

####Make the Frames

The script makeFrames.py will load the json data for each frame and create a new black frame with the yellow caption.

####Clone the Frames
	
This piece of the code takes each newlly created black frame and clones it 75 times. Since we extracted, originally 1 frame of the film each 3 seconds at 25fps, it means 1 of each 75 frames where saved and analyzed. This code will make sure that each frame is multiplied 75 times and saved to the data/out/full folder.

####Make the Film

This last script will take all the captioned frames (100200 in total), add the audio track and render a new video file saved as: data/film/out.mp4

The sound used has been previously edited in order to cut out the first minute which is not used during the film.	