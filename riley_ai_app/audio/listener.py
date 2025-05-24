import speech_recognition as sr

class VoiceListener:
    def __init__(self, hotword="Hey Riley"):
        self.hotword = hotword
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_hotword(self):
        with self.microphone as source:
            print("Listening for hotword...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                transcription = self.recognizer.recognize_google(audio)
                if self.hotword.lower() in transcription.lower():
                    return True
            except sr.UnknownValueError:
                return False
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return False

    def listen(self):
        with self.microphone as source:
            print("Listening for command...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                transcription = self.recognizer.recognize_google(audio)
                return transcription
            except sr.UnknownValueError:
                return "Sorry, I did not understand that."
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"