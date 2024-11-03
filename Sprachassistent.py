import configparser
import elevenlabs
import openai
import speech_recognition as sr

config = configparser.ConfigParser()
config.read('config.ini')

openai.api_key = config.get('API_KEYS', 'OPENAI_API_KEY')
elevenlabs.set_api_key(config.get('API_KEYS', 'ELEVENLABS_API_KEY'))

class SpeechRecognizer:
    def recognize_speech(self):
        # Nutze das Mikrofon als Audioquelle
        with sr.Microphone() as source:
            print("Sage etwas...")
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        try:
            # Verwende Google Speech Recognition, um den gesprochenen Text zu erkennen
            text = recognizer.recognize_google(audio, language="de-DE")
            print(f"Du hast gesagt: {text}")
            return text
        except sr.UnknownValueError:
            print("Spracherkennung konnte nichts verstehen.")
        except sr.RequestError as e:
            print(f"Fehler bei der Google Speech Recognition API: {e}")

if __name__ == "__main__":
    speech_recognizer = SpeechRecognizer()
    spoken_text = speech_recognizer.recognize_speech()
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=spoken_text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )


    print(response.choices[0].text)


    # Antwort zu Audio convertieren und wiedergeben
    audio = elevenlabs.generate(
        text=response.choices[0].text,
        voice="Daniel",
        model="eleven_multilingual_v2"
    )

    print("\nAI:", response.choices[0].text, end="\r\n")

    elevenlabs.play(audio)
