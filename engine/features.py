from playsound import playsound

import eel
import re
import pywhatkit as kit


from engine.command import speak
from engine.config import ASSISTANT_NAME


# Function to play assistant sound


@eel.expose

def playAssistantSound():
    music_dir = "forentend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("opening " + query)
        os.system("start " + query)
    
    else:
        speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    #define regular expression pattern to extract search term
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    #use re.search to find the term
    match = re.search(pattern, command, re.IGNORECASE)  
    #if a match is found,return the extracted song name ; otherwiswe return None
    return match.group(1) if match else None



