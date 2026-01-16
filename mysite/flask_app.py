

import os
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
ALLOWED_EXTENSIONS={'mp3'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/trading')
def trading_page():
    with open('earn_dates.txt', 'r') as file:
        file_content = file.read()
    return f"<pre>{file_content}</pre>"


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

os.startfile("http://127.0.0.1:5000/trading")

if __name__ == '__main__':
    app.run()


#http://127.0.0.1:5000/trading


"""


import os


from flask import Flask, render_template
app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/')
def index():
    files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html',files=files)






import os
from flask import Flask, request, render_template, jsonify
app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/translate',methods=['POST'])
def translate():
    data=request.json
    result="bark"
    converted = {
                    "translation":result
                }
    return jsonify(converted)
@app.route('/',methods=['GET'])
def index():
    files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html',files=files)
"""

"""
import os
from flask import Flask, request, render_template



app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/', methods=['GET', 'POST'])

@app.route('/translate', methods=['POST'])
def do_translate():
    ...


def index():
    files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    result=""
    if request.method == 'POST':
        result = "meow"
    return render_template('info34.html', files=files, result=result)



import os
from flask import Flask, request, render_template, jsonify
app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/')
def index():
    files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html',files=files)
@app.route('/translate',methods=['POST'])
def translate_route():
    data=request.get_json()
    text=data.get('text')
    result="meow"
    return jsonify({'result':result})

"""
