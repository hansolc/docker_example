csv to redis
============

Dockerfile: building image base on ubuntu:latest and installing redis-server

> docker run -it [imageId]
> redis-server &

In app.py, by 'docker inspect [container Id], check out the container ip and put it into redis instance

app.py: This will store to redis-server key: 0 to 181 numbers of data which is in csv file
Check out the key,value by redis-cli
