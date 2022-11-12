FROM python:3.7
WORKDIR /task
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8082
COPY . .
CMD ["flask", "run", "-p", "8082"]
