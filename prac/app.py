import redis

conn = redis.Redis(host='172.17.0.2', port=6379, db=0)
data = conn.get('myid')
print(data)
