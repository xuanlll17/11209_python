from flask import Blueprint,render_template,request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,EmailField,BooleanField,DateField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length,Regexp,Optional,EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

blueprint_auth = Blueprint('auth', __name__, url_prefix='/auth')  #/auth網址名稱

class MyForm(FlaskForm):
    email = StringField('郵件', validators=[DataRequired()])
    uPass = PasswordField('密碼', validators=[DataRequired(),Length(min=4,max=20)])

@blueprint_auth.route('/',methods=['GET','POST'])  #/auth會到這裡
@blueprint_auth.route('/login',methods=['GET','POST'])  #/auth/login, 後面不會有分號  #/auth和/auth/login會指向同一個網頁
@blueprint_auth.route('/login/<email>')
def login(email:str | None = None):  #名稱不重要
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if request.form['name'] == "12345" and request.form['password'] == "12345":
            print("密碼正確")
            return redirect("/auth/success")
        else:
            print("密碼錯誤")
    else:
        if email is not None:
            form.email.data = email
    return render_template("/auth/login.html",form=form)  #以templates為基準

@blueprint_auth.route('/success')
def success():
    return render_template('/auth/success.html')

class UserRegistrationForm(FlaskForm):
    uName = StringField("姓名",validators=[DataRequired(message="此欄必須有資料"),Length(min=2,max=20)])
    uGender = SelectField("性別",choices=[("女","女"),("男","男"),("其他","其他")])
    StringField("聯絡電話",validators=[])
    uPhone = StringField("聯絡電話",validators=[Regexp(r'\d\d\d\d-\d\d\d-\d\d\d',message="格式不正確")])
    uEmail = EmailField("電子郵件",validators=[DataRequired()])
    isGetEmail = BooleanField("接受促銷email",default=True)
    uBirth = DateField("出生年月日",validators=[Optional()],format='%Y-%m-%d')
    uAboutMe = TextAreaField("自我介紹", [Optional(),Length(max=200)])
    uPass = PasswordField("密碼",validators=[DataRequired(),Length(min=4,max=20),EqualTo('uConfirmPass',message='驗證密碼不正確')])  #validators需要__init__->DataRequired需要()
    uConfirmPass = PasswordField("驗證密碼",validators=[DataRequired(),Length(min=4,max=20)])

@blueprint_auth.route('/register',methods=['GET','POST'])
def register():
    form = UserRegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            uName = form.uName.data
            #form.uName.data = ''
            print("姓名",uName)

            uGender = form.uGender.data
            print("性別",uGender)

            uPhone = form.uPhone.data
            print("手機號碼",uPhone)
            
            uEmail = form.uEmail.data
            print("電子郵件",uEmail)

            isGetEmail = form.isGetEmail.data
            print("接受促銷","接受" if isGetEmail else "不接受")  #如果True傳出接受,如果False則傳出不接受

            uBirth = form.uBirth.data
            print("出生年月日",uBirth)

            uAboutMe = form.uAboutMe.data
            print("自我介紹",uAboutMe)

            uPass = form.uPass.data
            print("密碼",uPass)

            hash_password:str = generate_password_hash(uPass,method='pbkdf2:sha256',salt_length=8)
            #print(hash_password)
            #print("密碼正確" if check_password_hash(hash_password,uPass) else "密碼錯誤")

            conn_token = secrets.token_hex(16)

            return redirect(f'/auth/login/{uEmail}')
        else:
            print("驗證失敗")

    return render_template('/auth/register.html',form=form)