FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN apk update && apk add --virtual build-dependencies build-base gcc wget git libffi-dev
RUN pip install -r ./requirements.txt

CMD ["python", "start.py"]
