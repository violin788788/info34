

"""
meow
"""




from flask import Flask, render_template
app=Flask(__name__)
#MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/')
def index():
    #files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html')





"""
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
