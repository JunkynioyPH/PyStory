# PyStory

**A Base-Game Template that allows for creation of Text-based/Visual-Novel/Date-sim type game, with ease (for me at least)**

# Gist of its functionality

- It allows for basic dialogue printing in the `Native CMD Window` (`CMD`), emulating the effect of typing and backspacing characters, with customisable "typing speed," "Character Name," etc.
- Printing `CMD` `"ASCII"/"Art"/"Graphics"` for printing a big `Title_Name` in `Menus` and such.
- Printing text as it is styled with colours using `Rich`. `(colors are limited to the CMD it is ran on)`
- Pop up dialogues similar to `Windows` using `Ttk/Tkinter`; With customisable `title & subtitle` as well as windows `title bar` and `customisable sound` of when it pops up.
- `load/save` progress whether inventory or chapter progress `(N/A)`
- settings for volume and other things you might add. `(N/A) [I plan to make it somewhat modular]`
- Trigger a `funny haha` of your choice when a `key-word` is inserted. `(just look at the code for what i mean)`
- Display `Images` using `tkinter, canvas.create_image()`
- Display `Videos`, idk `(N\A)`
- Ability to manipulate `Mouse/Keyboard Inputs` using `PyAutoGui`, Mainly because I cannot be bothered to use other means.
- Find `WindowNameTitles` using `PyGetWindow` "Automatically" moving them using PyAutoGui. `(see `[PyStory/DevTools/](https://github.com/JunkynioyPH/PyStory/tree/master/devTools)`)`
- All of this will be consolidated into different easy-to-understand function/class names in an `importable 'essential.py' (with descriptions)` in every chapterX.py  for ease of creating a ChapterX.py `(see `[PyStory/Chapters/](https://github.com/JunkynioyPH/PyStory/tree/master/Chapters)`)`
- Much more `(Either it is not implemented yet or I have forgotten.)`

I Plan to use this to create a**`[Text-based Visual-Novel Date-sim RPG Horror Scary???]`** type game with 4th wall breaking stuff `(DDLC Inspired :) )`.

Biggest project I've worked on yet!

Please refer to the issues tab if any issues, duh.

# Pre-Requisites
## (`Python 3.10.x+ & make sure you have Ttk/TKinter Ticked!`)

Requires **`python 3.10.x+ & Ttk/TKinter`** to be installed.

## (`pip install ttkthemes`) ``OPTIONAL``

Requires **`ttkthemes`** to be installed for DarkMode.

## (`pip install pygame`)

Requires **pygame** to be installed.

## (`pip install pyautogui`)

Requires **pyautogui** to be installed.

## (`pip install rich`)

Requires **rich** to be installed.

# Fingers Crossed

Hope that everything works as it should!
