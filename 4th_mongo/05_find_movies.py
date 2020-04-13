from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


# target_movie = db.movies.find_one({})
db.movies.update_many({'star': '9.38'}, {'$set': {'star' : '0.00'}})
