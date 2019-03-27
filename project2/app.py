import redis
import time

redisClient = redis.StrictRedis(host='172.17.0.2', port=6379)

start_time = time.time()
for row in range(0,50000):
	redisClient.hmset(row, {"test1":row, "test2":row, "test3":row, "test4":row})
print(time.time() - start_time)

print("success")
