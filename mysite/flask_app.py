
import os
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    # Path to the static folder
    static_folder = os.path.join(app.root_path, 'static')
    # Get a list of all files in the static folder ending with .mp3
    mp3_files = []
    if os.path.exists(static_folder):
        mp3_files = [f for f in os.listdir(static_folder) if f.endswith('.mp3')]
    # Pass the list of files to your HTML template
    return render_template('info34.html', mp3_files=mp3_files)
if __name__ == '__main__':
    app.run(debug=True)
