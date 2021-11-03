FROM python:3.8-alpine

EXPOSE 5000/tcp

COPY code /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
