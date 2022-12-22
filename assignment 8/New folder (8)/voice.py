import gtts
sent=input("write:")
voice=gtts.gTTS(sent)
voice.save("b.mp3")