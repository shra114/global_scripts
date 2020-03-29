import os
import sys
import time

sleep_time = int(float(sys.argv[1])*60)

duration = 1  # seconds
freq = 440  # Hz

while(1):
	os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
	print (time.localtime())
	time.sleep(sleep_time)
