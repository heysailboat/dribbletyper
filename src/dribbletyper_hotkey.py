try: 
    import pyautogui
    import random
    import time
    import pyperclip
    from pynput import keyboard
except (ModuleNotFoundError, ImportError) as e:
    print(f"Error: {e}")
    print("------------------------------")
    print("Required modules not found. Would you like to automatically install them now? (y/n)")
    choice = input("> ").strip().lower()
    if choice == "y":
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui", "pyperclip", "pynput"])
        print("Modules installed. Please restart the script.")
    elif choice == "n":
        print("Exiting script. Please install the required modules and try again.")
        print("Run the following command to install the required modules:")
        print("pip install pyautogui pyperclip pynput")
        exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# ============================================================
# DRIBBLETYPER
# ============================================================
# Tweak the values below to change behaviour.
#
# THINKING_CHANCE:
#   Chance (0-1) of a random thinking pause per character.
#
# TYPO_CHANCE:
#   Chance (0-1) of making a typo before correcting it.
# ============================================================


THINKING_CHANCE = 0.002
TYPO_CHANCE = 0.001

START_DELAY = input("Enter start delay (seconds, default 5): ")
if not START_DELAY.strip():
    START_DELAY = 5
if not START_DELAY.isdigit():
    print("Invalid input. Using default value of 5 seconds.")
    START_DELAY = 5
if int(START_DELAY) < 0:
    print("Negative input. Using default value of 5 seconds.")
    START_DELAY = 5
else:
    START_DELAY = int(START_DELAY)

print("Choose speed multiplier:")
for i,v in enumerate((1.0,1.5,2.0,3.0,5.0),1):
    print(f"{i}) {v}")
print("6) Custom")
c=input("> ")
SPEED_MULTIPLIER={ "1":1.0,"2":1.5,"3":2.0,"4":3.0,"5":5.0}.get(c)
if SPEED_MULTIPLIER is None:
    if c=="6":
        SPEED_MULTIPLIER=float(input("Enter speed multiplier: "))
    else:
        SPEED_MULTIPLIER=5.0

print("Choose pyautogui pause time:")
for i,v in enumerate((0,0.01,0.02,0.05,0.1),1):
    print(f"{i}) {v}")
print("6) Custom")
c=input("> ")
PAUSE={ "1":0,"2":0.01,"3":0.02,"4":0.05,"5":0.1}.get(c)
if PAUSE is None:
    if c=="6":
        PAUSE=float(input("Enter pyautogui pause time: "))
    else:
        PAUSE=0
        
pyautogui.PAUSE = PAUSE

keyboard_neighbors = {
    'a':"sqzw",'b':"vghn",'c':"xdfv",'d':"serfcx",'e':"wsdr",'f':"drtgvc",
    'g':"ftyhbv",'h':"gyujnb",'i':"ujko",'j':"huikmn",'k':"jiolm",'l':"kop",
    'm':"njk",'n':"bhjm",'o':"iklp",'p':"ol",'q':"wa",'r':"edft",'s':"awedxz",
    't':"rfgy",'u':"yhji",'v':"cfgb",'w':"qase",'x':"zsdc",'y':"tghu",'z':"asx"
}

print("Choose WPM:")
for i,v in enumerate((35,55,75,95),1):
    print(f"{i}) {v}")
print("5) Custom")
c=input("> ")
wpm={ "1":35,"2":55,"3":75,"4":95}.get(c)
if wpm is None:
    if c=="5":
        wpm=float(input("Enter WPM: "))
    else:
        wpm=55

# Average chars/sec (~6 chars/word)
base_delay=(60/(wpm*6))/SPEED_MULTIPLIER
MIN_DELAY=base_delay*0.8
MAX_DELAY=base_delay*1.2

last_right_option = 0
typing = False

def type_clipboard():
    text = pyperclip.paste()

    if not text.strip():
        print("Clipboard is empty.")
        return

    print(f"Loaded {len(text):,} characters from clipboard.")

    print("\nClick target window.")
    for i in range(START_DELAY, 0, -1):
        print(f"Starting in {i}...", end="\r")
        time.sleep(1)

    current_delay = random.uniform(MIN_DELAY, MAX_DELAY)

    def pause(a, b):
        time.sleep(random.uniform(a, b) / SPEED_MULTIPLIER)

    for ch in text:
        current_delay += random.uniform(-base_delay * 0.08, base_delay * 0.08)
        current_delay = max(MIN_DELAY, min(MAX_DELAY, current_delay))

        if random.random() < THINKING_CHANCE:
            pause(0.30, 1.20)

        if ch.lower() in keyboard_neighbors and random.random() < TYPO_CHANCE:
            wrong = random.choice(keyboard_neighbors[ch.lower()])
            if ch.isupper():
                wrong = wrong.upper()
            pyautogui.write(wrong)
            pause(0.03, 0.08)
            pyautogui.press("backspace")
            pause(0.02, 0.06)

        pyautogui.write(ch)

        if ch in ".!?":
            pause(0.03, 0.08)
        elif ch == ",":
            pause(0.02, 0.05)
        elif ch in ";:":
            pause(0.03, 0.07)
        elif ch == "\n":
            pause(0.04, 0.08)
        else:
            time.sleep(current_delay)

    print("\nDone.\n")

def on_press(key):
    global last_right_option, typing

    try:
        if key == keyboard.Key.alt_r:
            now = time.time()

            if now - last_right_option < 0.4 and not typing:
                typing = True
                time.sleep(0.5)  # gives you time to release the key

                try:
                    type_clipboard()
                finally:
                    typing = False

            last_right_option = now

    except Exception as e:
        print(e)

print("\nDouble-tap Right Option (⌥) to type the clipboard.")
print("Press Ctrl+C in this terminal to quit.\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()