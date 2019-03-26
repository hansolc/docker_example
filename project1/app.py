from flask import Flask
import redis
import os
import socket
import csv

redisClient = redis.StrictRedis(host='localhost', port=6379)
mycsv = csv.reader(open("driving_score_180ea.csv"))
app = Flask(__name__)

@app.route("/")
def fpage():
	for row,i in zip(mycsv, range(182)):
		data = redisClient.hmset(i, {"compliance":row[0], "acceleration":row[1], "decelration":row[2], "result":row[3]})

	html = "<h3>Data Result</h3>" \
		"<b>compliance: </b> {data}<br/>"

	return html.format(data = redisClient.hget(1,"compliance"))

if __name__ == "__main__":
	app.run('0.0.0.0', port=4000)
