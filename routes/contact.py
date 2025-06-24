from flask import Blueprint, get_flashed_messages, render_template, request, flash, redirect, url_for
from flask_mail import Message
import os


contact = Blueprint("contact", __name__)


@contact.route("/contact", methods=["GET", "POST"])
def contact_form():
    from app import mail  # Lazy import to avoid circular dependency
    
    if request.method == 'POST':
        name = request.form.get('name')  
        furigana = request.form.get('furigana')  
        email = request.form.get('email')  
        email_confirm = request.form.get('email_confirm')
        phone = request.form.get('phone')  
        company = request.form.get('company', '')  # allow company to be optional
        message = request.form.get('message') 

        if not name:
            flash('必須項目に入力してください。', 'name_error')
        if not email:
            flash('必須項目に入力してください。', 'email_error')
        if not email_confirm:
            flash('必須項目に入力してください。', 'email_confirm_error')
        if not phone:
            flash('必須項目に入力してください。', 'phone_error') 
        if not message:
            print("Message field is empty")
            flash('必須項目に入力してください。', 'message_error')

        if email and email_confirm and  email != email_confirm:
            flash('メールアドレスが一致しません。もう一度ご確認ください。', 'validation_error')

        if get_flashed_messages(with_categories=True):
            flash('入力内容に問題があります。確認して再度お試しください。', 'form_error')
            return render_template('contact.html', form_data=request.form)

        body = f"""【Unni ホームページお問い合わせ】
お名前: {name}
フリガナ: {furigana}
メールアドレス: {email}
電話番号: {phone}
会社名: {company or '（未記入）'}
メッセージ:
{message}
"""

        try:
            msg = Message(subject='【Unni】お問い合わせ',
                          recipients=[os.environ.get('MAIL_USERNAME')],
                          body=body)
            mail.send(msg)
            flash('送信が完了しました。ありがとうございました！', 'success')
        except Exception as e:
            print('送信エラー:', e)
            flash('送信に失敗しました。時間をおいて再試行してください。', 'error')

        return redirect(url_for('contact.contact_form"'))

    return render_template('contact.html')

