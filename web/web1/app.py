from flask import Flask, url_for, render_template
import random
import pandas as pd
from auth import auth
from bs import bootstrap


app = Flask(__name__)
# 註冊blueprint
app.register_blueprint(auth.bp)
# 註冊bootstrap
app.register_blueprint(bootstrap.bp)

@app.route('/')
def index():
    # print('debug')      # 出現在終端機
    name = 'xxx'
    dataFrame = get_dataFrame()
    return render_template('index.html', name=name, dataFrame=dataFrame)

def get_dataFrame()->pd.DataFrame:
    data = [['xxx', 67, 82, 44],
            ['ooo', 95, 33, 24],
            ['yyy', 100, 70, 80]]
     
    return pd.DataFrame(data, columns=['姓名', '國文', '英文', '數學'])

#jinja
#{% ... %} 不會傳出值
#{{ ... }} 會傳出值

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>User {username}</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'<h1>Post {post_id * 5}</h1>'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'<h1>Subpath {subpath}</h1>'

@app.route('/url')
def url():
    print(url_for('hello'))
    print(url_for('show_user_profile', username = 'xuan'))
    print(url_for('static', filename = 'css/style.css'))
    return "ABC"       # 一定要return