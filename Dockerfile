FROM python:3.10-alpine
COPY . /EvilomaFamily
RUN pip install -r /EvilomaFamily/requirements.txt
WORKDIR /EvilomaFamily
CMD ["python", "start.py"]