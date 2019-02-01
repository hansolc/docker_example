from flask import flask
from redis import Redis
import os

# flaks 객체 생성
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# app.route: user가 localhost:[port number]에 접속시 실행되는 함수
# 만약 @app.route('/about') 으로 설정시 user 가 localhost:[port#]/about 에서 해당 script 실행
@app.route('/')
def home():
	redis.incr('hits')		# redis.incr([keyname]): incr key 값에 매칭되는 value +1
	return 'hellow world i have seen %s times' % redis.get('hits')

# script 실행시 실행.
if __name__=="__main__":
	app.run(host="0.0.0.0", debug=True)
