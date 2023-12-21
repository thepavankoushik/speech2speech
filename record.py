import sounddevice as sd
import scipy.io.wavfile as wv
import numpy as np



def record_audio(duration=5, freq=44100):
    print("Recording starts...")
    recording = sd.rec(int(duration * freq), 
                  samplerate=freq, channels=1)
    sd.wait()

    print("Recording done!")
    wv.write("input_audio/recording.wav", freq, recording)
    print("Saved the recording as recording.wav")

if __name__ == "__main__":
    record_audio()