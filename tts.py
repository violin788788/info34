
from piper import PiperVoice
import wave

voice = PiperVoice.load("en_US-lessac-medium.onnx")

text = "Welcome to your offline text to speech file on PythonAnywhere."

with wave.open("output.wav", "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print("Done - output.wav created")


"""
import pyttsx4,sys
engine = pyttsx4.init()


voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print("Voice", i)
    print("Name:", voice.name)
    print("ID:", voice.id)
    print()

#sys.exit()

#engine.setProperty('voice', 'english')

engine.setProperty('voice', 'english-us')


text_to_speak = "Welcome to your offline text to speech file on PythonAnywhere."
output_file = 'output.mp3'
engine.save_to_file(text_to_speak, output_file)
engine.runAndWait()
print(f"Success! Offline audio saved as {output_file}")
"""