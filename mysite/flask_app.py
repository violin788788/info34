# A very simple Flask Hello World app for you to get started with...
#from flask import Flask


import os
from flask import Flask, render_template
app=Flask(__name__)
MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/')
def index():
    files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('info34.html',files=files)


"""
from flask import Flask, render_template, request, send_file
from pydub import AudioSegment
import os
#from flask import Flask, render_template
app = Flask(__name__)
os.makedirs('uploads', exist_ok=True)
UPLOAD_FOLDER = 'uploads'
@app.route('/', methods=['GET', 'POST'])
#@app.route('/')
def run():
    if request.method == 'POST':
        # Get uploaded file and form inputs
        file = request.files['audio']
        start_time = int(request.form['start_time'])
        end_time = int(request.form['end_time'])
        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        # Load audio and clip it
        audio = AudioSegment.from_file(file_path)
        clipped_audio = audio[start_time*1000:end_time*1000]  # Clip in milliseconds
        # Save clipped audio
        clipped_path = 'clipped_audio.wav'
        clipped_audio.export(clipped_path, format='wav')
        # Send the clipped audio file as a response
        return send_file(clipped_path, as_attachment=True)
    files = os.listdir(UPLOAD_FOLDER)
    # Default rendering of the form
    return render_template('info.html', files=files)
"""