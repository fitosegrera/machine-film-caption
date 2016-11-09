import os

fps = 25
stepInSeconds = 3
stepInFrames = fps * stepInSeconds 

frame_files = 0

for f in os.listdir('data/out/'):
	frame_files += 1

index = 0
print "Total frames to clone", frame_files
print "Each frame will be cloned", stepInFrames, "times"
print "For a total of", frame_files*stepInFrames, "files"

for frame in range(frame_files):
	for i in range(index + 1, (stepInFrames*(frame+1))+1):
		os.system("cp data/out/" + str(frame+1) + ".png data/out/full/" + str(i) + ".png")
		index += 1
	print frame, "cloned!"

print "FINISHED!"