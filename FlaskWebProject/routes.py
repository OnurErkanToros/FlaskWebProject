from datetime import datetime
from flask_mail import Message
from flask import flash, redirect, render_template, request, session, url_for
from sqlalchemy import desc, true
from atmacaFlask import app, db, mail
from atmacaFlask.forms import EtkinlikveDuyuruForm, IletisimForm, LoginForm, PDFForm
from atmacaFlask.models import Activities, AnaHizmet, Announcement, User
from flask_login import login_required, login_user, current_user, logout_user
months = {'01': 'Ocak',
          '02': 'Şubat',
                '03': 'Mart',
                '04': 'Nisan',
                '05': 'Mayıs',
                '06': 'Haziran',
                '07': 'Temmuz',
                '08': 'Ağustos',
                '09': 'Eylül',
                '10': 'Ekim',
                '11': 'Kasım',
                '12': 'Aralık'}


@app.route('/')
def tanitim():
    return render_template('acilis.html')


@app.route('/anasayfa')
def index():
    title = "Atmaca & Karaarslan"
    duyurular = Announcement.query.order_by(
        desc(Announcement.announcementAddDate)).all()
    return render_template('anasayfa.html', duyurular=duyurular, title=title, calismaSaati=calismaSaati())


@app.route('/biz')
def biz():
    title = 'Biz'
    return render_template('biz.html', title=title, calismaSaati=calismaSaati())


@app.route('/hizmetlerimiz')
def hizmetler():
    title = 'Hizmetlerimiz'
    return render_template('hizmetler.html', title=title, calismaSaati=calismaSaati())


@app.route('/hizmetlerimiz/<hizmetId>')
def hizmetDetay(hizmetId):
    hizmet = AnaHizmet.query.filter_by(id=hizmetId).first()
    title = hizmet.baslik
    if not hizmet:
        return redirect(url_for('hizmetler'))
    return render_template('hizmetlerdetay.html', hizmet=hizmet, title=title, calismaSaati=calismaSaati())


@app.route('/iletisim', methods=['GET', 'POST'])
def iletisim():

    iletisimForm = IletisimForm()
    if request.method == 'POST' and iletisimForm.validate:
        print(iletisimForm.isim.data)
        msg = Message(sender="yourmail",
                      recipients=["yourmail"])
        msg.subject = iletisimForm.konu.data
        msg.body = f'Atmaca&Karaarslan sitesine bir mesaj var\nİsim: {iletisimForm.isim.data}\nEmail: {iletisimForm.mailAdres.data}\n\n{iletisimForm.mesaj.data}'
        mail.send(msg)
        flash('Mesajınız tarafımıza iletildi, en kısa sürede mail ile size ulaşacağız.')
        return redirect(url_for('iletisim'))
    title = 'İletişim'
    return render_template('iletisim.html', title=title, form=iletisimForm, calismaSaati=calismaSaati())


@app.route('/kariyer', methods=['GET', 'POST'])
def kariyer():
    pdfForm = PDFForm(request.form)
    if request.method == 'POST' and pdfForm.submit():
        msg = Message(sender="yourmail",
                      recipients=["yourmail"])
        msg.subject = 'Kariyer PDF'

        msg.body = f'Dosya gönderildi:'+pdfForm.file.gettext()
        fileData = request.files[pdfForm.file.name].read()
        msg.attach(pdfForm.file.name,
                   'application/pdf', fileData)
        mail.send(msg)
        return redirect(url_for('kariyer'))
    title = 'Kariyer'
    return render_template('kariyer.html', title=title, form=pdfForm, calismaSaati=calismaSaati())


@app.route('/kurumsal')
def kurumsal():
    title = 'Kurumsal'
    return render_template('kurumsal.html', title=title, calismaSaati=calismaSaati())


@app.route('/mevzuat')
def mevzuat():
    title = 'Mevzuat'
    return render_template('mevzuat.html', title=title, calismaSaati=calismaSaati())


@app.route('/etkinlikler')
def etkinlik():
    etkinlikler = Activities.query.order_by(
        desc(Activities.activityAddDate)).all()

    title = 'Etkinlikler'
    return render_template('etkinlikler.html', title=title, etkinlikler=etkinlikler, months=months, calismaSaati=calismaSaati())


@app.route('/duyurular')
def duyuru():
    duyurular = Announcement.query.order_by(
        desc(Announcement.announcementAddDate)).all()
    title = 'Duyurular'
    return render_template('duyurular.html', title=title, duyurular=duyurular, months=months, calismaSaati=calismaSaati())
# hizmetler detay eksik.


@app.route('/admin', methods=['GET', 'POST'])
def adminLogin():
    if current_user.is_authenticated:
        return redirect(url_for('adminEtkinlik'))
    loginForm = LoginForm()
    if request.method == 'POST' and loginForm.validate_on_submit():
        user = User.query.filter_by(email=loginForm.mail.data).first()
        if user and user.password == loginForm.parola.data:
            login_user(user=user)
            print('Giriş başarılı')
            return redirect(url_for('adminEtkinlik'))
    return render_template('admin/login.html', form=loginForm)


@app.route('/admin/etkinlikler', methods=['GET', 'POST'])
@login_required
def adminEtkinlik():
    etkinlikForm = EtkinlikveDuyuruForm()
    etkinlikler = Activities.query.order_by(
        desc(Activities.activityAddDate)).all()
    if request.method == 'POST' and etkinlikForm.validate_on_submit:
        etkinlik = Activities(etkinlikForm.title.data, etkinlikForm.subtitle.data,
                              etkinlikForm.text.data, etkinlikForm.announcementActivityDate.data, None)
        db.session.add(etkinlik)
        db.session.commit()
        return redirect(url_for('adminEtkinlik'))
    return render_template('admin/etkinlikler.html', form=etkinlikForm, etkinlikler=etkinlikler)


@app.route('/admin/duyurular', methods=['GET', 'POST'])
@login_required
def adminDuyuru():
    duyuruForm = EtkinlikveDuyuruForm()
    duyurular = Announcement.query.order_by(
        desc(Announcement.announcementAddDate)).all()
    if request.method == 'POST' and duyuruForm.validate_on_submit:
        duyuru = Announcement(duyuruForm.title.data, duyuruForm.subtitle.data,
                              duyuruForm.text.data, duyuruForm.announcementActivityDate.data, None)
        db.session.add(duyuru)
        db.session.commit()
        return redirect(url_for('adminDuyuru'))
    return render_template('admin/duyurular.html', form=duyuruForm, duyurular=duyurular)


@app.route('/admin/cikisYap')
@login_required
def logout():
    logout_user()
    return redirect(url_for('adminLogin'))


@app.route('/admin/etkinlikSil/<etkinlik_id>')
@login_required
def etkinlikSil(etkinlik_id):
    etkinlik = db.session.query(Activities).filter(
        Activities.id == etkinlik_id).one()
    db.session.delete(etkinlik)
    db.session.commit()
    print('Silme isteği yollandı', etkinlik.title)
    return redirect(url_for('adminEtkinlik'))


# @app.route('/admin/etkinlikDuzenle/<etkinlik_id>')
# @login_required
# def etkinlikDuzenle(etkinlik_id):
#     etkinlik = db.session.query(Activities).filter(
#         Activities.id == etkinlik_id).one()
#     form = EtkinlikveDuyuruForm()
#     form.title.data = etkinlik.title
#     form.subtitle.data = etkinlik.subtitle
#     form.text.data = etkinlik.text
#     form.announcementActivityDate.data = etkinlik.activityDate
#     form.addButton.label.text = 'Kaydet'
#     if request.method == 'POST' and form.validate_on_submit and (form.title.data != etkinlik.title or form.subtitle.data != etkinlik.subtitle or form.text.data != etkinlik.text):
#         db.session.add(
#             {Activities.title: form.title.data, Activities.subtitle: form.subtitle.data, Activities.text: form.text.data, Activities.activityDate: form.announcementActivityDate.data})
#         db.session.delete(etkinlik)
#         db.session.commit()
#     return render_template('admin/etkinlikler.html', form=form, baslik=True)


@app.route('/admin/duyuruSil/<duyuru_id>')
@login_required
def duyuruSil(duyuru_id):
    duyuru = db.session.query(Announcement).filter(
        Announcement.id == duyuru_id).one()
    db.session.delete(duyuru)
    db.session.commit()
    print('Silme isteği yollandı', duyuru.title)
    return redirect(url_for('adminDuyuru'))


def calismaSaati():
    now = datetime.now()
    if now.weekday() < 5:
        return now.time().hour < 18 and now.time().hour > 7
    else:
        return False
