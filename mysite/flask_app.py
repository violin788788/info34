
"""
import os,platform
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
os_name = platform.system()
app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
ALLOWED_EXTENSIONS={'mp3'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if 'file' in request.files:
            file=request.files['file']
            if file.filename!='' and allowed_file(file.filename):
                filename=secure_filename(file.filename)
                file.save(os.path.join(MP3S_FOLDER,filename))
                return redirect(url_for('index'))
    files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html',files=files)
"""


import os,platform,sys
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
os_name = platform.system()
app = Flask(__name__)
MP3S_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'mp3s')
EARNINGS_FILE = os.path.join(os.path.dirname(__file__), 'static', 'earn_dates.txt')
ALLOWED_EXTENSIONS = {'mp3'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(MP3S_FOLDER, filename))
                return redirect(url_for('index'))
    files = [f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    try:
        with open(EARNINGS_FILE, 'r') as file:
            earnings_data = file.read().splitlines()
            print(earnings_data)
            #sys.exit()
    except FileNotFoundError:
        earnings_data = ['Earnings dates file not found.']
    return render_template('info34.html', files=files, earnings=earnings_data)



if "Windows" in os_name:
    os.startfile("http://127.0.0.1:5000")
    if __name__ == '__main__':
        app.run()
