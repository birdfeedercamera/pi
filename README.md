https://twitch.tv/birdfeedercamera<br>
https://twitch.tv/bendingunit15


1. Enable Camera<br>
<code>sudo raspi-config</code>
2. Update repositories and install docker, git, python3, pip3 and docker-compose.<br>
<code>sudo apt-get update && sudo apt-get install docker.io python3 python3-pip git -y && pip3 install docker-compose</code>
3. Git clone the repo to your PI.<br>
<code>gh repo clone birdfeedercamera/pi</code><br>
3. Change Directory to the folder downloaded and open the "birdfeeder" directory. Open and edit "start_stream.py" and enter you twitch stream ID at the end. 
4. Run the following to command to start docker and run the birdfeedercamera container<br>
<code>docker-compose up --build</code>

