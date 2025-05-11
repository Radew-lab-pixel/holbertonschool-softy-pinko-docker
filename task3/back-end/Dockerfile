FROM ubuntu:latest
RUN apt-get update && \
  apt-get upgrade -y

RUN apt install -y python3 && \
  apt install -y python3-pip && \
  apt install -y python3-flask && \
  apt install -y python3-flask-cors
  
CMD ["echo", "Hello World"]
