FROM raspbian/stretch:latest

RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install ffmpeg python3 python3-pip libraspberrypi-bin -y
RUN usermod -a -G video root


COPY . .
# runs Python3 command in the container
CMD ["python3", "./start_stream.py"]
