FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN apk update
RUN pip install -r ./requirements.txt

CMD ["python", "start.py"]
