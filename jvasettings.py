import pyttsx3 

engine = pyttsx3.init()

rate = engine.getProperty("rate")
engine.setProperty("rate", 185)

voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)

volume = engine.getProperty("volume")
engine.setProperty("volume", 2.0)
