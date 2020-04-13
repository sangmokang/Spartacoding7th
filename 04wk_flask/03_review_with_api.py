from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    # //API = 약속이라고 했습니다! 이 약속을 서버에서부터 시작해보겠습니다.
# 리뷰를 작성하기 위해 필요한 정보는 다음 세 가지 입니다.
# - 제목(title)
# - 저자(author)
# - 리뷰(review)
#
# 따라서 서버 로직은 다음 세 단계로 구성되어야 합니다.
# 1. 클라이언트가 준 title, author, review 가져오기.
# 2. DB에 정보 삽입하기
# 3. 성공 여부 & 성공 메시지 반환하기

    title_recieve = request.form['title_give']
    author_recieve = request.form['author_give']
    review_recieve = request.form['review_give']

    db.reviews.insert_one({
        "title" : title_recieve,
        "author" : author_recieve,
        "review": review_recieve
    })

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})



@app.route('/reviews', methods=['GET'])
def read_reviews():
    # 모든    reviews의     문서를     가져온 후     list로     변환합니다.
    # 2. 성공 메시지와 함께 리뷰를 보냅니다.
    reviews = list(db.reviews.find({}, {'_id': False}))

    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)