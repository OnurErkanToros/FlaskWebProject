from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, DateField, FileField
from wtforms.validators import DataRequired, Length

class IletisimForm(FlaskForm):
    isim = StringField(label='İsim', validators=[DataRequired(
        message="Lütfen isminizi giriniz"), Length(min=2)])
    mailAdres = StringField(label='Mail', validators=[DataRequired()])
    konu = StringField(label='Konu', validators=[DataRequired(
        message='Lütfen geçerli bir konu giriniz')])
    mesaj = TextAreaField(label='Mesaj', validators=[
                          DataRequired(message='Lütfen mesajınızı giriniz')])
    gonderButton = SubmitField('Gönder')


class LoginForm(FlaskForm):
    mail = StringField('Email', validators=[DataRequired()])
    parola = PasswordField(label='Parola', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    girisButton = SubmitField('Giris Yap')


class EtkinlikveDuyuruForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    subtitle = StringField(validators=[DataRequired()])
    text = TextAreaField(validators=[DataRequired()])
    announcementActivityDate = DateField(validators=[DataRequired()])
    addButton = SubmitField(label='Ekle')

class PDFForm(FlaskForm):
    file=FileField('PDF dosyanızı buradan yükleyebilirsiniz', validators=[DataRequired()])
    submit=SubmitField('Dosyayı Gönder')