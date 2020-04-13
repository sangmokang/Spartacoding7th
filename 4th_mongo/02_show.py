from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

# MongoDB에서 데이터 모두 보기
# all_users = list(db.users.find())

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
john = list(db.users.find({'location': True}, {'_id': False}))

for user in john:
    print(user)

# print(all_users[0])         # 0번째 결과값을 보기'name'을 보기
#
# for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
#     print(user)