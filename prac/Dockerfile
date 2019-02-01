FROM frolvlad/alpine-python3

WORKDIR /app

COPY . /app

RUN pip3 install redis

CMD ["python3", "app.py"]
