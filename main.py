# main.py

from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
from io import BytesIO

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name,
                           last_name=current_user.last_name, email=current_user.email,
                           file_name=current_user.file_name, file_word_count=current_user.file_word_count)


@main.route('/profile/download')
@login_required
def download():
    return send_file(BytesIO(current_user.file_data), attachment_filename='file.txt', as_attachment=True)
