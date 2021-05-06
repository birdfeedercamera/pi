https://twitch.tv/birdfeedercamera<br>
https://twitch.tv/bendingunit15


1. Enable Camera<br>
<code>sudo raspi-config</code>
2. Update repositories and install docker, git, python3, pip3 and docker-compose.<br>
<code>sudo apt-get update && sudo apt-get install docker.io python3 python3-pip git -y && pip3 install docker-compose</code>
3. Git clone the repo to your PI.<br>
<code>gh repo clone birdfeedercamera/pi</code><br>
3. Open and edit "start_stream.py" and add your RTMP url and stream key to the file. 
4. Go back to the PI directory and run the following to command to start the docker container<br>
<code>docker-compose up --build</code>

