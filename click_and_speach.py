from pynput.mouse import Listener
import os
import random

phrase_dict = ( 
    "pourquoi tu fais ça",
    "wouaff wouaff",
    "j aime la quand tu clique",
    "Tu va y arriver",
    "non non non",
    "je crois pas que c est ça",
    "Hum",
    "hello world",
    "ça c est bien",
    "oulala"
)
mylist= [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
def phraseRandom():
    x = random.sample(mylist, 1)
    phrase = phrase_dict[random.choice(x)]
    try: 
        print(phrase)
        os.system("say {}".format(phrase))
    except (TypeError, NameError):
        pass

def on_click(x, y, button, pressed):
    if(pressed):
        print('Mouse Press')
        try:
            phraseRandom()
        except (TypeError, NameError):
            pass
        
def on_move(x, y):
    print("Mouse moved")
def on_scroll(x, y, dx, dy):
    print("Mouse scrolled")

# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()

with Listener(on_click=on_click) as listener:
    listener.join()