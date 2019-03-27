import redis
import time

redisClient = redis.StrictRedis(host='172.17.0.2', port=6379)

start_time = time.time()
for row in range(0,50000):
	redisClient.hmset("case", {"test1{}".format(row):row})
print(time.time() - start_time)

print("success")
