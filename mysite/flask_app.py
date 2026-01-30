import os,platform,sys
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
os_name = platform.system()
MP3S_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'mp3s')
#EARNINGS_FILE = os.path.join(os.path.dirname(__file__), 'static', 'earn_dates.txt')
#EARNINGS_FILE = os.path.join(os.path.dirname(__file__),'earn_dates.txt')
ALLOWED_EXTENSIONS = {'mp3'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
@app.route('/earnings')
def earnings():
    return render_template('earnings.html')
@app.route('/datetimes')
def datetimes():
    return render_template('datetimes.html')
@app.route('/developments')
def developments():
    return render_template('developments.html')
@app.route('/vote34')
def vote34():
    return render_template('vote34.html')
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(MP3S_FOLDER, filename))
                return redirect(url_for('main'))
    files = [f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html', files=files)


"""

def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(MP3S_FOLDER, filename))
                return redirect(url_for('index'))
    files = [f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html', files=files)

"""

print("os_name","=",os_name)
if "Windows" in os_name:
    os.startfile("http://127.0.0.1:5000")
    if __name__ == '__main__':
        app.run()
