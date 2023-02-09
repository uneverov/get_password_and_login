# docker run -d --net="host" server:1.0
FROM python:3
RUN apt update
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN git clone https://github.com/uneverov/get_password_and_login
WORKDIR get_password_and_login
CMD [ "python", "-u", "./server.py" ]