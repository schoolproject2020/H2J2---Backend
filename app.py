from flask import Flask
from flask import render_template
from models import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://" 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
# app.config['SECRET_KEY'] = 'sdfsdfsdddf'
# app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30) # 세션유지 시간을 30분으로 지정

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
