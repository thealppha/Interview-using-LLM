import wavio as wv
import sounddevice as sd

class Record:
    def __init__(self, duration):
        self.freq = 44100
        self.duration = duration
        
    def record_voice(self):
        recording = sd.rec(int(self.duration * self.freq),
                        samplerate=self.freq, channels=2)

        sd.wait()
        wv.write("recording.wav", recording, self.freq, sampwidth=2)