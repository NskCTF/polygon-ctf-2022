FROM alpine
RUN apk add python3 curl runuser
RUN adduser -D -u 1000 -g '' limiteduser

WORKDIR /app
COPY server.py .