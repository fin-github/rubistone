import interactions as i
from os import listdir
from icecream import ic

def get_tkn():
    return "token"


intents = i.Intents.DEFAULT
bot = i.Client(intents=intents)

for filename in listdir("modules"):
    filename = filename.removesuffix(".py") # remove the .py from <modulename>.py
    
    importstatement = "modules." + filename
    
    try:
        bot.load_extension(importstatement)
    except Exception as e:
        ic("ERROR WHILE LOADING EXTENSION", importstatement, "ERROR:", e)
        
bot.start(get_tkn())