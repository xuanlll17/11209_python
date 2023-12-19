from flask import Blueprint,render_template,request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length

blueprint_auth = Blueprint('auth', __name__, url_prefix='/auth')  #/auth網址名稱

class MyForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])

@blueprint_auth.route('/',methods=['GET','POST'])  #/auth會到這裡
@blueprint_auth.route('/login',methods=['GET','POST'])  #/auth/login, 後面不會有分號  #/auth和/auth/login會指向同一個網頁
def login():  #名稱不重要
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if request.form['name'] == "12345" and request.form['password'] == "12345":
            print("密碼正確")
            return redirect("/auth/success")
        else:
            print("密碼錯誤")
    return render_template("/auth/login.html",form=form)  #以templates為基準

@blueprint_auth.route('/success')
def success():
    return render_template('/auth/success.html')

class UserRegistrationForm(FlaskForm):
    uName = StringField("姓名",validators=[DataRequired(message="此欄必須有資料"),Length(min=2,max=20)])
@blueprint_auth.route('/register',methods=['GET','POST'])
def register():
    form = UserRegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            uName = form.uName.data
            form.uName.data = ''
            print(uName)
    return render_template('/auth/register.html',form=form)