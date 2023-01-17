FROM ubuntu:20.04
WORKDIR /app
ADD . /app
RUN apt-get update
RUN apt-get -y install python3.8 python3-pip
RUN python3.8 -m pip install --upgrade pip==21.1.2
RUN pip install -r requirements.txt

#CMD flask --app server.py run
CMD ["python3.8","./server.py"]
#CMD ["uwsgi","config.ini"]
EXPOSE 8083
