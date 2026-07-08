# DribbleTyper
Why type when you can just get this thing to do it for you?

This is a Python utility/script that simulates somewhat realistic human typing by typing the contents of your clipboard into the currently focused window. It has small variations in typing speed, occasional pauses, and optional typing mistakes\* to produce more natural-looking input.

Designed for when you don't whant to type out what your AI's given you, but you can't copy paste because it looks weird on version history.

###### \*: Note: it only automatically fixes some typos. Working on a fix.

---

## Features

* Types directly from your clipboard
* Adjustable typing speed
* Human-like timing with random speed variation
* Random "thinking" pauses
* Occasional typo simulation with semi-automatic correction\*\*
* Configurable countdown before typing begins
* Optional global hotkey version
* Cross-platform support (Windows, macOS, Linux)

###### \*\*: Again, note: it only automatically fixes some typos. Still working on a fix.

---

## Files

### `dribbletyper.py`

The standard version.

After copying text to your clipboard, simply press **Enter** in the terminal when you're ready to begin typing. It'll wait a set delay, and then begin.

### `dribbletyper_hotkey.py`

The hotkey version.

Instead of pressing Enter, this version waits for a global hotkey (currently a **double-tap of the Right Option (⌥) key on macOS**) before typing the clipboard contents.

The hotkey can be changed by modifying the `keyboard.Key` used inside the `on_press()` function.

###### Future versions will have a variable at the top.

---

## Requirements
### Both versions will automatically install their packages on first run. 

* Python 3.9 or newer

### Python packages

```bash
pip install pyautogui pyperclip pynput
```

or

```bash
pip install -r requirements.txt
```

Only the hotkey version requires `pynput`, but installing all three packages is recommended.

---

## Installation: Releases (Recommended)
1. Head over to the [Releases](https://github.com/heysailboat/dribbletyper/releases/latest) page in the right sidebar.
2. Download your chosen script.

## Installation: Cloning
Clone the repository:

```bash
git clone https://github.com/<username>/DribbleTyper.git
cd DribbleTyper
```

Install the required packages:

```bash
pip install pyautogui pyperclip pynput
```

If required packages are missing, the scripts can also automatically install them on first launch.

---

## Usage

### Standard Version

Run:

```bash
python dribbletyper.py
```

1. Copy the desired text to your clipboard.
2. Choose your settings.
3. Click the window you want to type into.
4. Press **Enter** in the terminal.
5. Wait for the countdown to finish.

---

### Hotkey Version

Run:

```bash
python dribbletyper_hotkey.py
```

1. Copy the desired text to your clipboard.
2. Choose your settings.
3. Click the destination window.
4. Trigger the configured hotkey.
5. Wait for the countdown to finish.

---

## Platform Support

| Platform        | Standard Version |              Hotkey Version             |
| --------------- | :--------------: | :-------------------------------------: |
| Windows         |         ✅        | ⚠️ Requires changing the default hotkey |
| macOS           |         ✅        |                    ✅                    |
| Linux (X11)     |         ✅        |                    ✅                    |
| Linux (Wayland) |    ⚠️ Limited    |                ⚠️ Limited               |

### macOS

The application must be granted **Accessibility** permission before it can simulate keyboard input. On most MacOS versions, it'll automatically open the System Preferences/Settings page for it

For the hotkey version, **Input Monitoring** permission may also be required depending on your macOS version.

### Windows

The standard version works without modification.

The hotkey version doesn't work out-of-the-box, it'll need some changing the hotkeys.

The hotkey version's default Right Option key should be changed to a Windows-friendly key, such as Right Shift.

<details>
<summary>Supported <code>pynput.keyboard.Key</code> values</summary>

### Modifier Keys

```python
keyboard.Key.alt_l
keyboard.Key.alt_r
keyboard.Key.alt_gr

keyboard.Key.ctrl_l
keyboard.Key.ctrl_r

keyboard.Key.shift_l
keyboard.Key.shift_r

keyboard.Key.cmd
keyboard.Key.cmd_l
keyboard.Key.cmd_r
```

---

### Lock Keys

```python
keyboard.Key.caps_lock
keyboard.Key.num_lock
keyboard.Key.scroll_lock
```

---

### Navigation Keys

```python
keyboard.Key.up
keyboard.Key.down
keyboard.Key.left
keyboard.Key.right

keyboard.Key.home
keyboard.Key.end
keyboard.Key.page_up
keyboard.Key.page_down

keyboard.Key.insert
keyboard.Key.delete
```

---

### Typing / Editing Keys

```python
keyboard.Key.enter
keyboard.Key.space
keyboard.Key.tab
keyboard.Key.backspace
keyboard.Key.delete
keyboard.Key.esc
```

---

### Function Keys

```python
keyboard.Key.f1
keyboard.Key.f2
keyboard.Key.f3
keyboard.Key.f4
keyboard.Key.f5
keyboard.Key.f6
keyboard.Key.f7
keyboard.Key.f8
keyboard.Key.f9
keyboard.Key.f10
keyboard.Key.f11
keyboard.Key.f12
```

(Some systems also expose F13–F20.)

---

### Media Keys *(availability depends on your keyboard and operating system)*

```python
keyboard.Key.media_play_pause
keyboard.Key.media_next
keyboard.Key.media_previous
keyboard.Key.media_volume_up
keyboard.Key.media_volume_down
keyboard.Key.media_volume_mute
```

---

### Miscellaneous Keys

```python
keyboard.Key.menu
keyboard.Key.pause
keyboard.Key.print_screen
```

---

### Recommended Hotkeys

| Key | Recommendation |
|------|----------------|
| `keyboard.Key.ctrl_r` | ⭐ Best overall |
| `keyboard.Key.scroll_lock` | ⭐ Great on full-size keyboards |
| `keyboard.Key.insert` | ⭐ Good alternative |
| `keyboard.Key.pause` | ⭐ Good if available |
| `keyboard.Key.alt_r` | ⚠️ Avoid on international keyboards (AltGr) |
| `keyboard.Key.ctrl_l` | ⚠️ Easy to trigger accidentally |
| `keyboard.Key.caps_lock` | ❌ Not recommended |

</details>

### Linux

The program works best on desktop environments using **X11**, including:

* Ubuntu
* Linux Mint
* Debian
* Fedora
* Arch Linux
* Pop!_OS
* EndeavourOS
* openSUSE

On Wayland-based systems, global keyboard hooks and simulated keyboard input may be restricted by the operating system.

Some distributions may also require a clipboard utility:

```bash
sudo apt install xclip
```

or

```bash
sudo apt install xsel
```

---

## Safety

DribbleTyper uses PyAutoGUI's built-in fail-safe.

If typing begins unexpectedly or you need to stop the automation immediately:

* Move your mouse to **any corner of your primary display**.
* PyAutoGUI will immediately raise a `FailSafeException` and stop typing.

You can also terminate the program with **Ctrl+C** while it is idle in the terminal.

---

## Configuration

The following settings can be adjusted when starting the program:

* Start delay
* Typing speed (WPM)
* Speed multiplier (hotkey version)
* PyAutoGUI pause time (hotkey version)

Internally, the following values can also be modified by editing the source code:

* `THINKING_CHANCE`
* `TYPO_CHANCE`

---

## Known Limitations

* The destination window must remain focused while typing.
* Some Unicode characters and symbols depend on your current keyboard layout.
* Certain applications (games, remote desktops, programs running as administrator, etc.) may block simulated keyboard input.
* Wayland may prevent keyboard simulation or global hotkeys due to security restrictions.
* Not all typos automatically fix.
* Not all keys can be typed. It has issues with apostrophes (').

---

## Disclaimer
###### (i was forced to include this)

This project is intended for automation, accessibility, testing, and educational purposes.

Please ensure that any automated typing complies with the rules and terms of service of the software or platform you are using.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
