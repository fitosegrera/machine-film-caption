import os

# use ffmpeg to extract 1 frame for every 3 seconds (-vf fps=1/3)
cmd = 'ffmpeg -r 25 -f image2 -s 640x480 -start_number 1 -i data/out/full/%01d.png -i data/film/Alloy-Orchestra-CUT.mp3 -acodec copy -vcodec libx264 -crf 25 -pix_fmt yuv420p data/film/out.mp4'
os.system(cmd)
print "DONE!"