from datetime import datetime
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# 파일 리스트
@app.route('/list')
def list_page():
    file_list = os.listdir("./uploads")
    html = """<center><a href="/">홈페이지</a><br><br>"""
    html += "file_list: {}".format(file_list) + "</center>"
    return html


# 업로드 HTML 렌더링
@app.route('/upload')
def upload_page():
    return render_template('upload.html')


# 파일 업로드 처리
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save('home/yewon/dataset/benign/' + secure_filename(f.filename))
        # f.save('./uploads/' + secure_filename(f.filename))
        return render_template('check.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
