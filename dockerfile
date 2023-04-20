FROM python:latest

WORKDIR /

COPY . /

CMD ["python3", "shadow.py"]