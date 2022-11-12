FROM ubuntu
RUN apt update
RUN apt install python3 -y

WORKDIR /app
COPY server.py .
COPY final/flag.txt /flag.txt