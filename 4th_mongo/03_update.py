from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

# 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })

db.users.update_one({'location': True},{'$set':{'age':'33'}})

user = db.users.find_one({'location':'Seoul'})
print (user)



