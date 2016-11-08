import os

# use ffmpeg to extract 1 frame for every 3 seconds (-vf fps=1/3)
cmd = 'ffmpeg -i data/film/Dziga-Vertov-Man-With-A-Movie-Camera.mp4 -vf fps=1/3 data/frames/$kino%01d.png'
os.system(cmd)
print "DONE!"