import subprocess
import os

# Path to your file
file_path = r"mysite\templates\info34.html"

# Optional: full path to Sublime Text executable if not in PATH
# For Windows, it might be something like:
# sublime_path = r"C:\Program Files\Sublime Text 3\sublime_text.exe"
#sublime_path = "sublime_text"  # assumes 'sublime_text' is in your system PATH

sublime_path = r"A:\Program Files\Sublime Text\sublime_text.exe"

# Make sure the file exists
if os.path.exists(file_path):
    subprocess.run([sublime_path, file_path])
else:
    print(f"File does not exist: {file_path}")
