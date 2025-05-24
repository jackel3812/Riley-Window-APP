from pyttsx3 import init

class Speaker:
    def __init__(self):
        self.engine = init()
        self.configure_voice()

    def configure_voice(self, voice_id=None, rate=150, volume=1.0):
        if voice_id:
            self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()