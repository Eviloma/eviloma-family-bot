FROM python:3.10-alpine
COPY . /eviloma-family-bot
RUN pip install -r /eviloma-family-bot/requirements.txt
WORKDIR /eviloma-family-bot
CMD ["python", "start.py"]