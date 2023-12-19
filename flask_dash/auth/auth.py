from flask import Blueprint,render_template,request

blueprint_auth = Blueprint('auth', __name__, url_prefix='/auth')  #/auth網址名稱

@blueprint_auth.route('/',methods=['GET','POST'])  #/auth會到這裡
@blueprint_auth.route('/login',methods=['GET','POST'])  #/auth/login, 後面不會有分號  #/auth和/auth/login會指向同一個網頁
def login():  #名稱不重要
    if request.method == "POST":
        print(request.form['email'])
        print(request.form['password'])
    return render_template("/auth/login.html")  #以templates為基準