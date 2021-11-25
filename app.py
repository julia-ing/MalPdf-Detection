from datetime import datetime
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session
import os
from libsvm_to_csv import print_result

from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload')
def upload_page():
    return render_template('upload.html')


@app.route('/result', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        
        os.system("rm -rf ../../../dataset/test ../test.txt ../cache-test ../cached-test.txt")
        os.system("mkdir ../../../dataset/test ../cache-test")

        f.save('../../../dataset/test/' + secure_filename(f.filename))
        os.system("ls -d ../../../dataset/test/* > ~/hidost/build/test.txt") 
        os.system("../src/cacher -i ../test.txt --compact --values -c /home/yewon/hidost/build/cache-test/ -t10 -m256")
        os.system("find /home/yewon/hidost/build/cache-test -name '*.pdf' -not -empty > ../cached-test.txt")
        os.system("cat ../cached-test.txt > ../cached-tests.txt")

        os.system("../src/pathcount -i ../cached-tests.txt -o ../test-pathcounts.bin")
        os.system("../src/feat-select -i ../test-pathcounts.bin -o ../test-features.nppf -m1")
        os.system("../src/feat-extract -b ../cached-tests.txt -m mal-test.txt -f ../features.nppf --values -o ../test-data.libsvm")
       
        result = print_result(f)
        #result = "test!!!"
        html = """<center><a href="/">Return to Home</a><br><br>"""
        html += "Result: {}".format(result) + "</center>"

        return html


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
