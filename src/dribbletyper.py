try: 
    import pyautogui
    import random
    import time
    import pyperclip
except (ModuleNotFoundError, ImportError) as e:
    print(f"Error: {e}")
    print("------------------------------")
    print("Required modules not found. Would you like to automatically install them now? (y/n)")
    choice = input("> ").strip().lower()
    if choice == "y":
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui", "pyperclip"])
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
# SPEED_MULTIPLIER:
#   1.0 = normal
#   2.0 = twice as fast
#   5.0 = very fast
#
# THINKING_CHANCE:
#   Chance (0-1) of a random thinking pause per character.
#
# TYPO_CHANCE:
#   Chance (0-1) of making a typo before correcting it.
# 
# pyautogui.PAUSE
#   Pause time between each pyautogui action (in seconds). 
#   Default is 0.1 for pyautogui, but we set it to 0 for this script to make it faster.
# ============================================================

SPEED_MULTIPLIER = 5.0

THINKING_CHANCE = 0.002
TYPO_CHANCE = 0.001

pyautogui.PAUSE = 0

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

while True:
    print("Copy the text you want to type to your clipboard.")
    input("Press Enter when you're ready...")

    type_clipboard()