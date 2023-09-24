FROM python:3.10
COPY . /EvilomaFamily
RUN pip install -r /EvilomaFamily/requirements.txt
WORKDIR /EvilomaFamily
CMD ["python", "start.py"]