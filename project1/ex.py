import redis
import csv

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
mycsv = csv.reader(open("driving_score_180ea.csv"))

hashName="man"

for row,i in zip(mycsv,range(182)):
	redisClient.hmset(i, {"compliance":row[0], "acceleration":row[1], "deceleration":row[2], "result":row[3]})

print(redisClient.hgetall(hashName))
