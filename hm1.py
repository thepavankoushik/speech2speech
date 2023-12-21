from speech2text import speech2text
from record import record_audio
from text2speech import say
from llm import chat

say("Hello PK Sir, How Can I Help You today?")
while True:
    record_audio()
    audio = "input_audio/recording.wav"
    text = speech2text(audio)
    user_input = text["text"]
    output = chat(user_input)
    say(output)
