from AppKit import NSSpeechSynthesizer
import time

nssp = NSSpeechSynthesizer.alloc().init()

desired_voice = None
for voice in NSSpeechSynthesizer.availableVoices():
    if "Rishi" in voice:
        desired_voice = voice
        break

nssp.setVoice_(desired_voice)

# Set rate and pitch
rate = 200  # Adjust the rate as needed
pitch = 50  # Adjust the pitch as needed

def say(text):
    nssp.startSpeakingString_(text)
    while nssp.isSpeaking():
        time.sleep(0.1)