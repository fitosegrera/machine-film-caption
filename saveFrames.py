import os

cmd = 'ffmpeg -i Dziga-Vertov-Man-With-A-Movie-Camera-\(1929\).mp4 -r 25/1 ../frames/$kino%01d.png'
os.system(cmd)
print "DONE!"