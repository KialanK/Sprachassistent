# Speech Assistant

This is a simple speech recognition and response program written in Python. It uses the microphone as an audio source, recognizes the spoken text using Google Speech Recognition, and generates a response using OpenAI's GPT-3.5-turbo-instruct engine. The response is then converted to audio and played back.

## Installation

To run this program, you need to have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

To install the dependencies specified in the `Pipfile`, navigate to the directory containing the `Pipfile` and run:

```bash
pipenv install
```

This will create a new virtual environment, if one doesn't already exist, and install the packages specified under the `[packages]` section. The packages currently specified are:

- assemblyai
- elevenlabs
- openai
- SpeechRecognition

To activate the virtual environment, run:

```bash
pipenv shell
```

Now, you can run your Python scripts within this environment, and they'll have access to the installed packages.
