FROM ubuntu:latest
RUN apt-get update && \
  apt-get upgrade -y

RUN apt install -y python3 && \
  apt install -y python3-pip && \
  apt install -y python3-flask
  
CMD ["echo", "Hello World"]
