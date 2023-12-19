from flask import Blueprint,render_template

blueprint_auth = Blueprint('auth', __name__, url_prefix='/auth')  #/auth網址名稱

@blueprint_auth.route('/')  #/auth會到這裡
@blueprint_auth.route('/login')  #/auth/login, 後面不會有分號  #/auth和/auth/login會指向同一個網頁
def login():  #名稱不重要
    return render_template("/auth/login.html")  #以templates為基準