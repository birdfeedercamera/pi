import subprocess
import time


def start_stream(timeout):
    date = time.strftime("%m-%d-%Y")
    print("Today is %s" % date) 
    return_code = subprocess.run("/opt/vc/bin/raspivid -ex auto -awb auto  -n -t 0 -w 1920 -h 1080 -fps 30 -b 3500000 -g 60 -o - | ffmpeg -f lavfi -i anullsrc -c:a aac -r 30 -i - -g 60 -strict experimental -threads 1 -vcodec copy -map 0:a -map 1:v -b:v 3500000 -preset medium -f flv rtmp://twitchstreamurl/twitchstreamID", shell=True, timeout=timeout)

    return_code = str(return_code)
    print(return_code[-2:-1])


while True:
    hour = int(time.strftime("%H"))
    active_hours = [7,8,9,10,11,12,13,14,15,16,17,18]
    if hour in active_hours:
            timeout =  (21 - hour ) * 60 * 60
            start_stream(timeout)
    else:
        time.sleep(600)

